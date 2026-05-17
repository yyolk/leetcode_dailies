# https://leetcode.com/problems/island-perimeter/


class Solution:
    """463. Island Perimeter

    You are given `row x col` `grid` representing a map where `grid[i][j] = 1`
    represents land and `grid[i][j] = 0` represents water.

    Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is
    completely surrounded by water, and there is exactly one island (i.e., one or more
    connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the
    water around the island. One cell is a square with side length 1. The grid is
    rectangular, width and height don't exceed 100. Determine the perimeter of the
    island.

    """

    def island_perimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0]) if grid else 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Each land cell contributes 4 to the perimeter

                    # Check if adjacent cells are also land cells
                    if i > 0 and grid[i - 1][j] == 1:
                        # Subtract 2 for each adjacent land cell horizontally
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        # Subtract 2 for each adjacent land cell vertically
                        perimeter -= 2

        return perimeter

    islandPerimeter = island_perimeter
