# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
from functools import lru_cache
from sys import maxsize


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
        n = len(job_difficulty)

        # If it's impossible to schedule the jobs in d days
        if n < d:
            return -1

        @lru_cache(maxsize=None)
        def dp(i: int, k: int) -> int:
            # Base case: if we have only one day left, the difficulty is the maximum
            # difficulty of the remaining jobs.
            if k == 1:
                return max(job_difficulty[i:])

            # Initialize the maximum difficulty for this subproblem
            max_difficulty = -1
            min_schedule_difficulty = maxsize

            # Iterate over possible partitions of the remaining jobs
            for j in range(i, n - k + 1):
                max_difficulty = max(max_difficulty, job_difficulty[j])
                rest_difficulty = dp(j + 1, k - 1)
                if rest_difficulty > -1:
                    min_schedule_difficulty = min(
                        min_schedule_difficulty, max_difficulty + rest_difficulty
                    )

            # If there is a valid partition, it won't be -1
            return min_schedule_difficulty

        # Return the result
        return dp(0, d)

    minDifficulty = min_difficulty
