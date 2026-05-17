# https://leetcode.com/problems/unique-paths-ii/


class Solution:
    """63. Unique Paths II

    You are given an `m x n` integer array `grid`. There is a robot initially located at
    the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the
    **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either
    down or right at any point in time.

    An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that
    the robot takes cannot include **any** square that is an obstacle.

    Return *the number of possible unique paths that the robot can take to reach the
    bottom-right corner*.

    The testcases are generated so that the answer will be less than or equal to `2 *
    109`.
    """

    def unique_paths_with_obstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Create a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left cell
        dp[0][0] = 1 if grid[0][0] == 0 else 0

        # Fill the first row
        for j in range(1, n):
            if grid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # Fill the first column
        for i in range(1, m):
            if grid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # Fill the rest of the array
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is in the bottom-right cell
        return dp[m - 1][n - 1]

    uniquePathsWithObstacles = unique_paths_with_obstacles
