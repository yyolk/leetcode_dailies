"""Submit a daily solution to LeetCode and format the ms/mb comment.

Uses the same unofficial endpoints the website uses. Session cookies belong
in GitHub Actions secrets, not in this repo.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import requests

from .constants import LEETCODE_BASE_URL

SLUG_RE = re.compile(r"/problems/([a-z0-9-]+)/?", re.IGNORECASE)
DATE_TITLE_RE = re.compile(r"^\d{8}$")
SUBMIT_MARKER_RE = re.compile(r"<!--\s*leetcode-submit\s+sha=(\S+)\s+id=(\S+)\s*-->")
TIME_LINE_RE = re.compile(r"^(?:[-*]\s*)?\d+(?:\.\d+)?\s*ms\b", re.IGNORECASE)
MEMORY_LINE_RE = re.compile(r"^(?:[-*]\s*)?\d+(?:\.\d+)?\s*mb\b", re.IGNORECASE)
PENDING_STATES = {"PENDING", "STARTED", "PENDING_REJUDGE"}
BEATS_THRESHOLD = 50


class SubmitError(RuntimeError):
    """LeetCode rejected the submission or the unofficial API failed."""


def slug_from_url(url: str) -> str | None:
    match = SLUG_RE.search(url or "")
    return match.group(1) if match else None


def slug_from_source(source: str) -> str | None:
    for line in source.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and "leetcode.com/problems/" in stripped:
            return slug_from_url(stripped)
    return None


def solution_path_for_date(root: Path, yyyymmdd: str) -> Path:
    return root / "solutions" / yyyymmdd[:4] / yyyymmdd[:6] / f"{yyyymmdd}.py"


def _is_ellipsis_stmt(stmt: ast.stmt) -> bool:
    return (
        isinstance(stmt, ast.Expr)
        and isinstance(stmt.value, ast.Constant)
        and stmt.value.value is Ellipsis
    )


def solution_is_unimplemented(source: str) -> bool:
    """True when a Solution method body is only a docstring plus `...`."""
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or node.name != "Solution":
            continue
        for item in node.body:
            if not isinstance(item, ast.FunctionDef):
                continue
            stmts = list(item.body)
            if (
                stmts
                and isinstance(stmts[0], ast.Expr)
                and isinstance(stmts[0].value, ast.Constant)
                and isinstance(stmts[0].value.value, str)
            ):
                stmts = stmts[1:]
            if not stmts or all(
                _is_ellipsis_stmt(stmt) or isinstance(stmt, ast.Pass) for stmt in stmts
            ):
                return True
    return False


def _numeric_metric(value: str, unit: str) -> str:
    text = value.strip().lower()
    text = text.replace("milliseconds", "ms").replace("megabytes", "mb")
    match = re.search(r"(\d+(?:\.\d+)?)", text)
    if match:
        return match.group(1)
    if text.endswith(unit):
        return text[: -len(unit)].strip() or text
    return text


def _format_percentile(percentile: float | int | None) -> str | None:
    if percentile is None:
        return None
    try:
        value = float(percentile)
    except (TypeError, ValueError):
        return None
    if value < BEATS_THRESHOLD:
        return None
    if value == int(value):
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _metric_bullet(value: str, unit: str, percentile: float | int | None) -> str:
    line = f"- {_numeric_metric(value, unit)}{unit}"
    beats = _format_percentile(percentile)
    if beats is not None:
        line += f" (beats {beats}%)"
    return line


def format_benchmark_comment(
    *,
    runtime: str,
    memory: str,
    yyyymmdd: str | None = None,
    runtime_percentile: float | int | None = None,
    memory_percentile: float | int | None = None,
    sha: str | None = None,
    submission_id: str | int | None = None,
) -> str:
    lines: list[str] = []
    if yyyymmdd:
        lines.extend([f"solution {yyyymmdd}.py", ""])
    lines.append(_metric_bullet(runtime, "ms", runtime_percentile))
    lines.append(_metric_bullet(memory, "mb", memory_percentile))
    if sha and submission_id is not None:
        lines.append(f"<!-- leetcode-submit sha={sha} id={submission_id} -->")
    return "\n".join(lines) + "\n"


def comment_for_notification(body: str) -> str:
    """Benchmark comment without the hidden submit marker."""
    return SUBMIT_MARKER_RE.sub("", body or "").strip()


def write_github_output(name: str, value: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    delimiter = "BENCH_EOF"
    with Path(path).open("a", encoding="utf-8") as handle:
        if "\n" in value:
            handle.write(f"{name}<<{delimiter}\n{value.rstrip()}\n{delimiter}\n")
        else:
            handle.write(f"{name}={value}\n")


def comment_already_has_benchmark(body: str, sha: str | None = None) -> bool:
    text = (body or "").replace("\r\n", "\n")
    if sha:
        match = SUBMIT_MARKER_RE.search(text)
        if match and match.group(1) == sha:
            return True
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return any(
        TIME_LINE_RE.search(line)
        and index + 1 < len(lines)
        and MEMORY_LINE_RE.search(lines[index + 1])
        for index, line in enumerate(lines)
    )


def parse_check_payload(payload: dict[str, Any]) -> dict[str, Any]:
    state = str(payload.get("state") or "").upper()
    status = str(payload.get("status_msg") or payload.get("status") or "")
    runtime = str(payload.get("status_runtime") or payload.get("runtime") or "")
    memory = str(payload.get("status_memory") or payload.get("memory") or "")
    runtime_percentile = payload.get("runtime_percentile")
    memory_percentile = payload.get("memory_percentile")
    return {
        "state": state,
        "status": status,
        "runtime": runtime,
        "memory": memory,
        "runtime_percentile": runtime_percentile,
        "memory_percentile": memory_percentile,
        "accepted": state == "SUCCESS" and status.lower() == "accepted",
        "pending": state in PENDING_STATES or not state,
        "raw": payload,
    }


def _session_headers(csrf: str, referer: str) -> dict[str, str]:
    return {
        "x-csrftoken": csrf,
        "referer": referer,
        "origin": LEETCODE_BASE_URL,
        "user-agent": "leetcode-dailies-submit/0.1",
        "content-type": "application/json",
    }


def _session_cookies(session: str, csrf: str) -> dict[str, str]:
    return {"LEETCODE_SESSION": session, "csrftoken": csrf}


def fetch_question_id(slug: str, session: str, csrf: str) -> str:
    query = {
        "query": """
            query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    titleSlug
                }
            }
        """,
        "variables": {"titleSlug": slug},
    }
    response = requests.post(
        f"{LEETCODE_BASE_URL}/graphql/",
        headers=_session_headers(csrf, f"{LEETCODE_BASE_URL}/problems/{slug}/"),
        cookies=_session_cookies(session, csrf),
        json=query,
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    question_id = data.get("data", {}).get("question", {}).get("questionId")
    if not question_id:
        raise SubmitError(f"Could not resolve questionId for slug {slug!r}: {data}")
    return str(question_id)


def submit_solution(
    *,
    slug: str,
    question_id: str,
    typed_code: str,
    session: str,
    csrf: str,
    lang: str = "python3",
) -> str:
    response = requests.post(
        f"{LEETCODE_BASE_URL}/problems/{slug}/submit/",
        headers=_session_headers(csrf, f"{LEETCODE_BASE_URL}/problems/{slug}/"),
        cookies=_session_cookies(session, csrf),
        json={"lang": lang, "question_id": str(question_id), "typed_code": typed_code},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    submission_id = payload.get("submission_id")
    if submission_id is None:
        raise SubmitError(f"Submit did not return submission_id: {payload}")
    return str(submission_id)


def poll_submission(
    submission_id: str,
    session: str,
    csrf: str,
    *,
    attempts: int = 60,
    delay_seconds: float = 2.0,
    sleeper=time.sleep,
    getter=None,
) -> dict[str, Any]:
    getter = getter or (
        lambda: requests.get(
            f"{LEETCODE_BASE_URL}/submissions/detail/{submission_id}/check/",
            headers=_session_headers(csrf, f"{LEETCODE_BASE_URL}/"),
            cookies=_session_cookies(session, csrf),
            timeout=30,
        )
    )
    last: dict[str, Any] | None = None
    for _ in range(attempts):
        response = (
            getter() if getter.__code__.co_argcount == 0 else getter(submission_id)
        )
        response.raise_for_status()
        last = parse_check_payload(response.json())
        if not last["pending"]:
            return last
        sleeper(delay_seconds)
    raise SubmitError(f"Timed out waiting for submission {submission_id}: {last}")


def post_pr_comment(pr_number: int, body: str) -> None:
    subprocess.run(
        ["gh", "pr", "comment", str(pr_number), "--body", body],
        check=True,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Path to YYYYMMDD.py")
    parser.add_argument("--slug")
    parser.add_argument("--question-id")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--sha")
    parser.add_argument("--title")
    parser.add_argument("--body-url", help="PR body or problem URL")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    root = Path.cwd()
    title = (args.title or "").strip()
    source_path = args.source
    if source_path is None and DATE_TITLE_RE.match(title):
        source_path = solution_path_for_date(root, title)
    if source_path is None:
        print("No solution path (pass --source or --title YYYYMMDD).", file=sys.stderr)
        return 1
    source = source_path.read_text(encoding="utf-8")

    if solution_is_unimplemented(source):
        print(f"Skipping submit; {source_path} is still a stub.")
        return 0

    slug = args.slug or slug_from_url(args.body_url or "") or slug_from_source(source)
    if not slug:
        print("Could not determine problem slug.", file=sys.stderr)
        return 1

    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = (
        os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
        or os.environ.get("LEETCODE_CSRFTOKEN", "").strip()
    )
    if not session or not csrf:
        print(
            "LEETCODE_SESSION and LEETCODE_CSRF_TOKEN are not set; "
            "skipping submit until secrets exist."
        )
        return 0

    if args.pr and not args.dry_run:
        try:
            comments_raw = subprocess.check_output(
                ["gh", "api", f"repos/{{owner}}/{{repo}}/issues/{args.pr}/comments"],
                text=True,
            )
            comments = json.loads(comments_raw)
            for comment in comments:
                if comment_already_has_benchmark(comment.get("body") or "", args.sha):
                    print(f"PR #{args.pr} already has a benchmark comment; skipping.")
                    return 0
        except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
            print(f"Could not list existing comments ({exc}); continuing.")

    if args.dry_run:
        print(f"Dry run: would submit {source_path} as {slug}")
        return 0

    question_id = args.question_id or fetch_question_id(slug, session, csrf)
    submission_id = submit_solution(
        slug=slug,
        question_id=question_id,
        typed_code=source,
        session=session,
        csrf=csrf,
    )
    print(f"Submitted {slug} as {submission_id}")
    result = poll_submission(submission_id, session, csrf)
    if not result["accepted"]:
        print(
            f"LeetCode {result['status'] or result['state']} for {slug} "
            f"(submission {submission_id})",
            file=sys.stderr,
        )
        return 2

    date_name = title if DATE_TITLE_RE.match(title) else None
    if date_name is None and DATE_TITLE_RE.match(source_path.stem):
        date_name = source_path.stem
    comment = format_benchmark_comment(
        runtime=result["runtime"],
        memory=result["memory"],
        yyyymmdd=date_name,
        runtime_percentile=result.get("runtime_percentile"),
        memory_percentile=result.get("memory_percentile"),
        sha=args.sha,
        submission_id=submission_id,
    )
    print(comment, end="")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        Path(summary).write_text(
            "## LeetCode submit\n\n" + comment,
            encoding="utf-8",
        )
    if args.pr:
        post_pr_comment(args.pr, comment)
        write_github_output("posted", "true")
        write_github_output("comment", comment_for_notification(comment))
        print(f"Posted benchmark comment on PR #{args.pr}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
