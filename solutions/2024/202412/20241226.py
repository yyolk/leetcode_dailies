# https://leetcode.com/problems/target-sum/


class Solution:
    """494. Target Sum

    You are given an integer array `nums` and an integer `target`.

    You want to build an **expression** out of nums by adding one of the symbols `'+'`
    and `'-'` before each integer in nums and then concatenate all the integers.

    * For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before
    `1` and concatenate them to build the expression `"+2-1"`.

    Return the number of different **expressions** that you can build, which evaluates
    to `target`."""

    def find_target_sum_ways(self, nums: list[int], target: int) -> int:
        # We'll use dynamic programming to solve this problem
        # dp[i][j] will represent the number of ways to reach sum j using the first i numbers

        total_sum = sum(nums)
        if abs(target) > total_sum:
            # If target sum is not possible to achieve
            return 0

        # Since we can have negative numbers, we need to shift everything by total_sum
        dp = [[0 for _ in range(2 * total_sum + 1)] for _ in range(len(nums) + 1)]

        # Base case: there's one way to achieve sum 0 with 0 numbers
        dp[0][total_sum] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * total_sum + 1):
                if dp[i - 1][j] > 0:
                    # We can either add or subtract the current number
                    # Adding nums[i-1]
                    dp[i][j + nums[i - 1]] += dp[i - 1][j]
                    # Subtracting nums[i-1]
                    dp[i][j - nums[i - 1]] += dp[i - 1][j]

        # The target shifted to non-negative index
        return dp[len(nums)][total_sum + target]

    findTargetSumWays = find_target_sum_ways
