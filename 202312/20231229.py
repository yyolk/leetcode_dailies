# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/


class Solution:
    """1335. Minimum Difficulty of a Job Schedule

    You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on
    the `ith` job, you have to finish all the jobs `j` where `0 <= j < i`).

    You have to finish **at least** one task every day. The difficulty of a job schedule
    is the sum of difficulties of each day of the `d` days. The difficulty of a day is
    the maximum difficulty of a job done on that day.

    You are given an integer array `job_difficulty` and an integer `d`. The difficulty
    of the `ith` job is `job_difficulty[i]`.

    Return *the minimum difficulty of a job schedule*. If you cannot find a schedule for
    the jobs return `-1`.
    """

    def min_difficulty(self, job_difficulty: list[int], d: int) -> int:
        ...

    minDifficulty = min_difficulty
