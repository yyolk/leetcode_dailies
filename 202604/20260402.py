# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn

class Solution:
    """3418. Maximum Amount of Money Robot Can Earn

    You are given an m x n grid. A robot starts at the top-left corner of the
    grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The
    robot can move either right or down at any point in time.
    The grid contains a value coins[i][j] in each cell:
    If coins[i][j] >= 0, the robot gains that many coins.
    If coins[i][j] < 0, the robot encounters a robber, and the robber steals the
    absolute value of coins[i][j] coins.
    The robot has a special ability to neutralize robbers in at most 2 cells on
    its path, preventing them from stealing coins in those cells.
    Note: The robot's total coins can be negative.
    Return the maximum profit the robot can gain on the route.
    """
    def maximum_amount(self, coins: list[list[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        NEG_INF = -10**18
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        # Initialize starting cell
        val = coins[0][0]
        dp[0][0][0] = val
        if val < 0:
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = coins[i][j]
                # Max incoming for each k (neutralizations used up to previous cell)
                incoming = [NEG_INF] * 3
                if j > 0:
                    for k in range(3):
                        incoming[k] = max(incoming[k], dp[i][j - 1][k])
                if i > 0:
                    for k in range(3):
                        incoming[k] = max(incoming[k], dp[i - 1][j][k])
                for prev in range(3):
                    if incoming[prev] == NEG_INF:
                        continue
                    # Option 1: do not neutralize (always valid)
                    dp[i][j][prev] = max(dp[i][j][prev], incoming[prev] + val)
                    # Option 2: neutralize if robber and slot remains
                    if val < 0 and prev < 2:
                        dp[i][j][prev + 1] = max(dp[i][j][prev + 1], incoming[prev])
        return max(dp[m - 1][n - 1])

    maximumAmount = maximum_amount