# https://leetcode.com/problems/climbing-stairs/


class Solution:
    """70. Climbing Stairs

    You are climbing a staircase. It takes `n` steps to reach the top.

    Each time you can either climb `1` or `2` steps. In how many distinct ways can you
    climb to the top?
    """

    def climb_stairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        # Base cases initialization
        dp[1] = 1
        dp[2] = 2

        # Calculate the number of ways for each step using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the number of ways to climb to the top
        return dp[n]

    climbStairs = climb_stairs
