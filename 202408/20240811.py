# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/


class Solution:
    """1568. Minimum Number of Days to Disconnect Island

    You are given an `m x n` binary grid `grid` where `1` represents land and `0`
    represents water. An **island** is a maximal **4\\-directionally** (horizontal or
    vertical) connected group of `1`s.

    The grid is said to be **connected** if we have **exactly one island**, otherwise is
    said **disconnected**.

    In one day, we are allowed to change **any** single land cell `(1)` into a water
    cell `(0)`.

    Return *the minimum number of days to disconnect the grid*.

    """
    # Direction vectors for moving up, down, left, and right
    def __init__(self):
        self.xDir = [0, 0, -1, 1]
        self.yDir = [-1, 1, 0, 0]

    # Check if the cell (i, j) is within bounds, unvisited, and is land (1)
    def is_safe(self, grid, i, j, visited):
        return (0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 1)

    # Recursive DFS function to mark all connected parts of land as visited
    def island_count(self, grid, i, j, visited):
        # Mark the current cell as visited
        visited[i][j] = True

        # Traverse all four possible directions
        for k in range(4):
            newRow = i + self.xDir[k]
            newCol = j + self.yDir[k]
            # If the new cell is safe, continue the DFS
            if self.is_safe(grid, newRow, newCol, visited):
                self.island_count(grid, newRow, newCol, visited)

    # Function to count the number of connected land components in the grid
    def count_land(self, grid, visited):
        count = 0
        # Iterate through all cells in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If we find unvisited land, start a new DFS
                if grid[i][j] == 1 and not visited[i][j]:
                    self.island_count(grid, i, j, visited)
                    count += 1
        return count

    def min_days(self, grid: list[list[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        # Initialize a visited array to track visited cells
        visited = [[False] * cols for _ in range(rows)]

        # Check how many connected land components exist initially
        count = self.count_land(grid, visited)

        # If more than one island or no land, no days are needed
        if count > 1 or count == 0:
            return 0

        # Simulate the removal of each land cell and check if it splits the island
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Temporarily remove the land cell
                    grid[i][j] = 0

                    # Check the number of components after removal
                    mat = [[False] * cols for _ in range(rows)]
                    count2 = self.count_land(grid, mat)

                    # Restore the removed cell
                    grid[i][j] = 1

                    # If the island is now split or there is no land, only one day is needed
                    if count2 > 1 or count2 == 0:
                        return 1

        # If removing one cell does not split the island, two days are needed
        return 2

    minDays = min_days
