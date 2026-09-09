from generate_active_daily.submit_solution import (
    comment_already_has_benchmark,
    format_benchmark_comment,
    parse_check_payload,
    slug_from_source,
    slug_from_url,
    solution_is_unimplemented,
    solution_path_for_date,
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
