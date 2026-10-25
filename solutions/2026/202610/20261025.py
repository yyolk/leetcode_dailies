# https://leetcode.com/problems/number-of-closed-islands/


class Solution:
    """1254. Number of Closed Islands

    Given a 2D `grid` consists of `0s` (land) and `1s` (water). An *island*
    is a maximal 4-directionally connected group of `0s` and a *closed
    island* is an island **totally** (all left, top, right, bottom)
    surrounded by `1s.`

    Return the number of *closed islands*.

    Constraints:

    * `1 <= grid.length, grid[0].length <= 100`

    * `0 <= grid[i][j] <= 1`
    """

    def closed_island(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            # Out of bounds or already water/visited.
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 0:
                return
            # Mark as visited by turning land into water.
            grid[r][c] = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc)

        # Flood all border-connected land so they cannot be closed islands.
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Count remaining islands; each is closed (interior only).
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)
        return count

    closedIsland = closed_island
