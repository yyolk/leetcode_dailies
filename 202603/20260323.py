# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix

class Solution:
    """1594. Maximum Non Negative Product in a Matrix
    
    You are given a m x n matrix grid. Initially, you are located at the top-left
    corner (0, 0), and in each step, you can only move right or down in the matrix.
    Among all possible paths starting from the top-left corner (0, 0) and ending in
    the bottom-right corner (m - 1, n - 1), find the path with the maximum non-
    negative product. The product of a path is the product of all integers in the
    grid cells visited along the path.
    Return the maximum non-negative product modulo 109 + 7. If the maximum
    product is negative, return -1.
    Notice that the modulo is performed after getting the maximum product.
    """
    def max_product_path(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 10**9 + 7
        # DP tables track max and min product reachable at each cell
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]
        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]
        # Fill first row (only right moves)
        for j in range(1, cols):
            val = max_dp[0][j - 1] * grid[0][j]
            max_dp[0][j] = val
            min_dp[0][j] = val
        # Fill first column (only down moves)
        for i in range(1, rows):
            val = max_dp[i - 1][0] * grid[i][0]
            max_dp[i][0] = val
            min_dp[i][0] = val
        # Fill remaining cells using max/min from up and left
        for i in range(1, rows):
            for j in range(1, cols):
                # All 4 candidate products from previous max/min * current cell
                candidates = [
                    max_dp[i - 1][j] * grid[i][j],
                    min_dp[i - 1][j] * grid[i][j],
                    max_dp[i][j - 1] * grid[i][j],
                    min_dp[i][j - 1] * grid[i][j],
                ]
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        # Max product at end; modulo only if non-negative
        max_val = max_dp[rows - 1][cols - 1]
        if max_val >= 0:
            return max_val % MOD
        return -1

    maxProductPath = max_product_path