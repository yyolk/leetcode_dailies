# https://leetcode.com/problems/number-of-islands/


class Solution:
    """200. Number of Islands

    Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and
    `'0'`s (water), return *the number of islands*.

    An **island** is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are all
    surrounded by water.

    """

    def num_islands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            grid[i][j] = "0"  # Mark the current cell as visited
            dfs(i + 1, j)  # Check down
            dfs(i - 1, j)  # Check up
            dfs(i, j + 1)  # Check right
            dfs(i, j - 1)  # Check left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count

    numIslands = num_islands
