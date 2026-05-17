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

    def binary_search(self, jobs, current_index):
        low, high = 0, current_index - 1

        while low <= high:
            mid = (low + high) // 2

            if jobs[mid][1] <= jobs[current_index][0]:
                if jobs[mid + 1][1] <= jobs[current_index][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1

        return -1

    def job_scheduling(
        self, start_time: list[int], end_time: list[int], profit: list[int]
    ) -> int:
        # Combine the information into tuples and sort them by end time
        jobs = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])

        n = len(jobs)

        # Create an array to store the maximum profit at each index
        dp = [0] * n

        # Base case: the maximum profit for the first job is its own profit
        dp[0] = jobs[0][2]

        for i in range(1, n):
            # Find the latest job that doesn't overlap with the current job
            prev_index = self.binary_search(jobs, i)

            # Calculate the maximum profit at the current index
            include_current = jobs[i][2] + (dp[prev_index] if prev_index != -1 else 0)
            exclude_current = dp[i - 1]
            dp[i] = max(include_current, exclude_current)

        return dp[-1]

    jobScheduling = job_scheduling
