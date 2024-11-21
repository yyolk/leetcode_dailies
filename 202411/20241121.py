# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/


class Solution:
    """2257. Count Unguarded Cells in the Grid

    You are given two integers `m` and `n` representing a **0\\-indexed** `m x n` grid.
    You are also given two 2D integer arrays `guards` and `walls` where `guards[i] =
    [rowi, coli]` and `walls[j] = [rowj, colj]` represent the positions of the `ith`
    guard and `jth` wall respectively.

    A guard can see **every** cell in the four cardinal directions (north, east, south,
    or west) starting from their position unless **obstructed** by a wall or another
    guard. A cell is **guarded** if there is **at least** one guard that can see it.

    Return *the number of unoccupied cells that are **not** **guarded**.*

    """

    def count_unguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        # Initialize grid with all cells unguarded
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # Function to mark cells in a direction from a given point
        def mark_direction(i, j, di, dj):
            while 0 <= i < m and 0 <= j < n:
                if grid[i][j] == 1 or grid[i][j] == -1:
                    # Wall or another guard stops vision
                    break
                if grid[i][j] == 0:
                    # Mark as guarded
                    grid[i][j] = 2
                i += di
                j += dj

        # Mark guards and walls
        for r, c in guards:
            # Mark guard
            grid[r][c] = 1

        for r, c in walls:
            # Mark wall
            grid[r][c] = -1

        # For each guard, mark all cells they can see
        for r, c in guards:
            # Right, Down, Left, Up
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                mark_direction(r + di, c + dj, di, dj)

        # Count unguarded cells
        unguarded_cells = sum(cell == 0 for row in grid for cell in row)

        return unguarded_cells

    countUnguarded = count_unguarded
