# https://leetcode.com/problems/minimum-falling-path-sum-ii/


class Solution:
    """1289. Minimum Falling Path Sum II

    Given an `n x n` integer matrix `grid`, return *the minimum sum of a **falling path
    with non-zero shifts***.

    A **falling path with non-zero shifts** is a choice of exactly one element from each
    row of `grid` such that no two elements chosen in adjacent rows are in the same
    column.

    """

    def min_falling_path_sum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Create a DP table to store minimum path sums
        dp = [[0] * n for _ in range(n)]
        # Initialize the first row of DP table with the first row of grid
        dp[0] = grid[0][:]

        # Iterate through rows starting from the second row
        for i in range(1, n):
            # Iterate through columns
            for j in range(n):
                # Calculate the minimum path sum to reach (i, j) by choosing the minimum path sum
                # from the previous row's adjacent positions and adding the current grid value
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1 :]) + grid[i][j]

        # Return the minimum sum from the last row of the DP table
        return min(dp[-1])

    minFallingPathSum = min_falling_path_sum
