# https://leetcode.com/problems/maximum-profit-in-job-scheduling/


class Solution:
    """1235. Maximum Profit in Job Scheduling

    We have `n` jobs, where every job is scheduled to be done from `start_time[i]` to
    `end_time[i]`, obtaining a profit of `profit[i]`.

    You're given the `start_time`, `end_time` and `profit` arrays, return the maximum
    profit you can take such that there are no two jobs in the subset with overlapping
    time range.

    If you choose a job that ends at time `X` you will be able to start another job that
    starts at time `X`.
    """

    def job_scheduling(
        self, start_time: list[int], end_time: list[int], profit: list[int]
    ) -> int:
        ...

    jobScheduling = job_scheduling
