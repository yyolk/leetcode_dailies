# https://leetcode.com/problems/painting-the-walls/
from sys import maxsize


class Solution:
    """2742. Painting the Walls

    You are given two **0-indexed** integer arrays, `cost` and `time`, of size `n`
    representing the costs and the time taken to paint `n` different walls respectively.
    There are two painters available:

    * A**paid painter** that paints the `ith` wall in `time[i]` units of time and takes
    `cost[i]` units of money.

    * A**free painter** that paints **any** wall in `1` unit of time at a cost of `0`.
    But the free painter can only be used if the paid painter is already **occupied**.

    Return *the minimum amount of money required to paint the* `n`*walls.*
    """

    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        """Minimum amount of money to paint the walls by simulating the scenario.

        Proposed solution using dynamic programming.

        Args:
            cost (list of int): Cost to paint n different walls.
            time (list of int): Time to paint n different walls.

        Returns:
            int: The minimum amount of money required to paint n walls.
        """
        n = len(cost)

        # Create a 2D DP array with dimensions (n + 1) x (n + 1).
        dp = [[maxsize for i in range(n + 1)] for j in range(n + 1)]

        # Initialize the DP array.
        dp[0][0] = 0  # No cost for painting 0 walls.

        for i in range(n):
            for j in range(n + 1):
                t = min(n, j + time[i] + 1)

                # Calculate the minimum cost when not using the paid painter.
                dp[i + 1][t] = min(dp[i + 1][t], dp[i][j] + cost[i])

                # Calculate the minimum cost when using the paid painter.
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

        # Return the minimum cost for painting all walls.
        return dp[n][n]
