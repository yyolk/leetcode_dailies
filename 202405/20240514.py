# https://leetcode.com/problems/path-with-maximum-gold/


class Solution:
    """1219. Path with Maximum Gold

    In a gold mine `grid` of size `m x n`, each cell in this mine has an integer
    representing the amount of gold in that cell, `0` if it is empty.

    Return the maximum amount of gold you can collect under the conditions:

    * Every time you are located in a cell you will collect all the gold in that cell.

    * From your position, you can walk one step to the left, right, up, or down.

    * You can't visit the same cell more than once.

    * Never visit a cell with `0` gold.

    * You can start and stop collecting gold from **any** position in the grid that has
    some gold.

    """

    def get_maximum_gold(self, grid: list[list[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            temp = grid[i][j]
            # Mark as visited
            grid[i][j] = 0
            max_gold = 0

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, temp + dfs(i + di, j + dj))

            # Revert back after exploration
            grid[i][j] = temp
            return max_gold

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold

    getMaximumGold = get_maximum_gold
