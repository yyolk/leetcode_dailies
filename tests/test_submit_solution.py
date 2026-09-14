import requests

from generate_active_daily.submit_solution import (
    AUTH_FAILED_EXIT,
    AuthFailedError,
    comment_already_has_benchmark,
    comment_for_notification,
    format_benchmark_comment,
    is_auth_http_error,
    parse_check_payload,
    raise_for_leetcode_status,
    slug_from_source,
    slug_from_url,
    solution_is_unimplemented,
    solution_path_for_date,
    write_github_output,
)


STUB = '''# https://leetcode.com/problems/two-sum/

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """doc"""
        ...

    twoSum = two_sum
'''

IMPLEMENTED = """# https://leetcode.com/problems/two-sum/

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need], index]
            seen[value] = index
        return []

    twoSum = two_sum
"""


class _FakeResponse:
    def __init__(self, status_code: int, text: str = "denied") -> None:
        self.status_code = status_code
        self.url = "https://leetcode.com/problems/rectangle-overlap/submit/"
        self.text = text

    def raise_for_status(self) -> None:
        raise requests.HTTPError(
            f"{self.status_code} Client Error",
            response=self,
        )


def test_slug_from_url_and_source():
    assert (
        slug_from_url(
            "https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/"
        )
        == "minimum-moves-to-clean-the-classroom"
    )
    assert slug_from_source(STUB) == "two-sum"


def test_solution_path_for_date(tmp_path):
    path = solution_path_for_date(tmp_path, "20260901")
    assert path == tmp_path / "solutions" / "2026" / "202609" / "20260901.py"


def test_unimplemented_detection():
    assert solution_is_unimplemented(STUB)
    assert not solution_is_unimplemented(IMPLEMENTED)


def test_format_benchmark_comment_matches_gate():
    body = format_benchmark_comment(
        runtime="12 ms",
        memory="17.4 MB",
        yyyymmdd="20260908",
        runtime_percentile=81.2,
        memory_percentile=40.0,
        sha="abc",
        submission_id=99,
    )
    assert body.splitlines()[0] == "solution 20260908.py"
    assert body.splitlines()[1] == ""
    assert body.splitlines()[2] == "- 12ms (beats 81.2%)"
    assert body.splitlines()[3] == "- 17.4mb"
    assert "sha=abc" in body
    assert comment_already_has_benchmark(body, "abc")
    # Any existing ms/mb pair is enough to skip a second submit.
    assert comment_already_has_benchmark(body, "other")
    assert not comment_already_has_benchmark("not a benchmark")
    visible = comment_for_notification(body)
    assert visible.startswith("solution 20260908.py")
    assert "leetcode-submit" not in visible


def test_format_benchmark_comment_omits_beats_below_fifty():
    body = format_benchmark_comment(
        runtime="0 ms",
        memory="19.2 MB",
        yyyymmdd="20260908",
        runtime_percentile=49.9,
        memory_percentile=50,
    )
    assert "- 0ms" in body
    assert "- 19.2mb (beats 50%)" in body
    assert "beats 49" not in body


def test_write_github_output_multiline(tmp_path, monkeypatch):
    output = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    write_github_output("posted", "true")
    write_github_output("comment", "solution 20260908.py\n\n- 0ms\n- 19.2mb")
    text = output.read_text(encoding="utf-8")
    assert "posted=true\n" in text
    assert "comment<<BENCH_EOF\n" in text
    assert "- 0ms\n- 19.2mb\nBENCH_EOF\n" in text


def test_parse_check_payload_states():
    accepted = parse_check_payload(
        {
            "state": "SUCCESS",
            "status_msg": "Accepted",
            "status_runtime": "8 ms",
            "status_memory": "16.2 MB",
            "runtime_percentile": 88.0,
            "memory_percentile": 12.5,
        }
    )
    assert accepted["accepted"]
    assert accepted["runtime_percentile"] == 88.0
    pending = parse_check_payload({"state": "PENDING"})
    assert pending["pending"]
    wrong = parse_check_payload({"state": "SUCCESS", "status_msg": "Wrong Answer"})
    assert not wrong["accepted"]
    assert not wrong["pending"]


def test_raise_for_leetcode_status_maps_403_to_auth_failed():
    try:
        raise_for_leetcode_status(_FakeResponse(403, "Forbidden"))
    except AuthFailedError as exc:
        assert "HTTP 403" in str(exc)
        assert "LEETCODE_SESSION" in str(exc)
        assert is_auth_http_error(exc.__cause__)
    else:
        raise AssertionError("expected AuthFailedError")


def test_raise_for_leetcode_status_maps_other_http_to_submit_error():
    try:
        raise_for_leetcode_status(_FakeResponse(500, "boom"))
    except AuthFailedError:
        raise AssertionError("500 should not be auth failure")
    except Exception as exc:
        assert "HTTP 500" in str(exc)
        assert not is_auth_http_error(exc.__cause__)
    else:
        raise AssertionError("expected SubmitError")

    assert AUTH_FAILED_EXIT == 3
