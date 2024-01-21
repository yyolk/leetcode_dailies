# https://leetcode.com/problems/house-robber/


class Solution:
    """198. House Robber

    You are a professional robber planning to rob houses along a street. Each house has
    a certain amount of money stashed, the only constraint stopping you from robbing
    each of them is that adjacent houses have security systems connected and **it will
    automatically contact the police if two adjacent houses were broken into on the same
    night**.

    Given an integer array `nums` representing the amount of money of each house, return
    *the maximum amount of money you can rob tonight **without alerting the police***.
    """

    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize an array to store the maximum amount robbed at each house
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Iterate through the rest of the houses
        for i in range(2, len(nums)):
            # The maximum amount at the current house is either the sum of the amount at the current house
            # and the amount two houses ago, or the amount at the previous house.
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        # The result is the maximum amount robbed from the last house
        return dp[-1]

    rob = rob
