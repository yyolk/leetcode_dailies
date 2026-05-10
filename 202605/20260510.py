# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index

class Solution:
    """2770. Maximum Number of Jumps to Reach the Last Index

    You are given a 0-indexed array nums of n integers and an integer target.
    You are initially positioned at index 0. In one step, you can jump from
    index i to any index j such that: 0 <= i < j < n and -target <= nums[j] -
    nums[i] <= target. Return the maximum number of jumps you can make to reach
    index n - 1. If there is no way to reach index n - 1, return -1.
    """
    def maximum_jumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # dp[i]: max jumps to reach i from 0, -1 if unreachable
        dp = [-1] * n
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                # check if i reachable and jump condition satisfied
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    # maximize jumps
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1]

    maximumJumps = maximum_jumps