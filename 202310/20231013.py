# https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    """746. Min Cost Climbing Stairs

    You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a
    staircase. Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index `0`, or the step with index `1`.

    Return *the minimum cost to reach the top of the floor*.
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Finds the minimum cost to reach the top of the floor.

        Proposed solution using dynamic programming.

        Args:
            cost (List of int): The cost where the index is mapped to the i_th step
                on the staircase.

        Returns:
            int: The minimum cost to reach the top.
        """
        n = len(cost)
        # Initialize the dp array with the cost of the first two steps
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Calculate the minimum cost for each step from the third step to the top
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # The minimum cost can be either starting from the last step or the second to
        # last step, this accounts for both possible starting positions.
        return min(dp[-1], dp[-2])
