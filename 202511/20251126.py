# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/


class Solution:
    """2435. Paths in Matrix Whose Sum Is Divisible by K

    You are given a 0-indexed m x n integer matrix grid and an integer k. You
    are currently at position (0, 0) and you want to reach position (m - 1, n -
    1) moving only down or right.

    Return the number of paths where the sum of the elements on the path is
    divisible by k. Since the answer may be very large, return it modulo 10^9 +
    7.
    """
    def number_of_paths(self, grid: list[list[int]], k: int) -> int:
        # Define modulo for large numbers
        MOD = 10**9 + 7
        # Extract dimensions
        m, n = len(grid), len(grid[0])
        # Initialize 3D DP: dp[i][j][r] = ways to reach (i,j) with sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        # Base case: start at (0,0) with sum = grid[0][0]
        dp[0][0][grid[0][0] % k] = 1
        # Fill DP table row by row, column by column
        for i in range(m):
            for j in range(n):
                # Skip base case
                if i == 0 and j == 0:
                    continue
                # Add paths from above (if possible)
                if i > 0:
                    for prev_r in range(k):
                        # New remainder after adding grid[i][j]
                        new_r = (prev_r + grid[i][j]) % k
                        # Accumulate ways modulo MOD
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i - 1][j][prev_r]) % MOD
                # Add paths from left (if possible)
                if j > 0:
                    for prev_r in range(k):
                        # New remainder after adding grid[i][j]
                        new_r = (prev_r + grid[i][j]) % k
                        # Accumulate ways modulo MOD
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j - 1][prev_r]) % MOD
        # Result: ways to end with sum % k == 0
        return dp[m - 1][n - 1][0]

    numberOfPaths = number_of_paths