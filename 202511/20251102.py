# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/


class Solution:
    """2257. Count Unguarded Cells in the Grid

    You are given two integers m and n representing a 0-indexed m x n grid. You
    are also given two 2D integer arrays guards and walls where
    guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions
    of the ith guard and jth wall respectively.

    A guard can see every cell in the four cardinal directions (north, east, south,
    or west) starting from their position unless obstructed by a wall or another
    guard. A cell is guarded if there is at least one guard that can see it.

    Return the number of unoccupied cells that are not guarded.
    """
    def count_unguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # Initialize grid with 0 for empty, will set 1 for wall, 2 for guard
        grid = [[0] * n for _ in range(m)]
        # Place walls on the grid
        for r, c in walls:
            grid[r][c] = 1
        # Place guards on the grid
        for r, c in guards:
            grid[r][c] = 2
        # Matrix to track seen (guarded) cells
        seen = [[False] * n for _ in range(m)]
        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # For each guard, simulate visibility in all directions
        for gr, gc in guards:
            for dr, dc in dirs:
                # Start from the cell next to the guard in this direction
                nr, nc = gr + dr, gc + dc
                # Continue until out of bounds or hit obstacle
                while 0 <= nr < m and 0 <= nc < n:
                    # If cell is wall or guard, stop without marking
                    if grid[nr][nc] == 1 or grid[nr][nc] == 2:
                        break
                    # Mark empty cell as seen
                    seen[nr][nc] = True
                    # Move to next cell in direction
                    nr += dr
                    nc += dc
        # Count unoccupied and unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                # Check if empty (0) and not seen
                if grid[i][j] == 0 and not seen[i][j]:
                    count += 1
        return count

    countUngaurded = count_unguarded