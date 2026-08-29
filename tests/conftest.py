import importlib.util
import os
from pathlib import Path

import pytest

SLOW_NAME_MARKERS = ("bruteforce", "brute_force", "exhaustive", "multi_row_samples")


def _is_slow_nodeid(nodeid: str) -> bool:
    lower = nodeid.lower()
    return any(marker in lower for marker in SLOW_NAME_MARKERS)


def pytest_collection_modifyitems(items):
    slow = pytest.mark.slow
    skip_slow = pytest.mark.skip(reason="slow tests run on the weekly job")
    skip_requested = os.environ.get("SKIP_SLOW") == "1"

    for item in items:
        name = item.name.lower()
        if any(marker in name for marker in SLOW_NAME_MARKERS):
            item.add_marker(slow)
        if item.get_closest_marker("slow"):
            if skip_requested:
                item.add_marker(skip_slow)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # xdist workers each invoke this hook; only the controller should write.
    if getattr(config, "workerinput", None) is not None:
        return
    if os.environ.get("PYTEST_XDIST_WORKER"):
        return

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    reports: dict[str, object] = {}
    for _status, entries in terminalreporter.stats.items():
        for report in entries:
            nodeid = getattr(report, "nodeid", None)
            if not nodeid:
                continue
            keywords = getattr(report, "keywords", {}) or {}
            if not (_is_slow_nodeid(nodeid) or "slow" in keywords):
                continue
            if getattr(report, "when", "call") not in {"call", "setup"}:
                continue
            existing = reports.get(nodeid)
            if existing is None or (
                getattr(report, "when", "") == "call"
                and getattr(existing, "when", "") != "call"
            ):
                reports[nodeid] = report

    if not reports:
        return

    lines = [
        "## Slow tests",
        "",
        "| Test | Status | Duration |",
        "| --- | --- | --- |",
    ]
    for nodeid in sorted(reports):
        report = reports[nodeid]
        status = getattr(report, "outcome", "unknown")
        duration = f"{getattr(report, 'duration', 0.0):.2f}s"
        if status == "skipped":
            duration = "\u2014"
        escaped = nodeid.replace("|", "\\|")
        lines.append(f"| `{escaped}` | {status} | {duration} |")
    lines.append("")
    table = "\n".join(lines)

    summary_file = Path(summary_path)
    existing_text = (
        summary_file.read_text(encoding="utf-8") if summary_file.exists() else ""
    )
    if "## Slow tests" not in existing_text:
        with summary_file.open("a", encoding="utf-8") as handle:
            handle.write(table)


@pytest.fixture
def solution(request):
    test_file = Path(str(request.node.path)).resolve()
    stem = test_file.stem
    assert stem.startswith("test_")

    date_code = stem.removeprefix("test_")
    assert len(date_code) == 8 and date_code.isdigit()

    root = Path(__file__).resolve().parents[1]
    path = root / "solutions" / date_code[:4] / date_code[:6] / f"{date_code}.py"

    spec = importlib.util.spec_from_file_location(f"daily_{date_code}", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)

    return module.Solution()
