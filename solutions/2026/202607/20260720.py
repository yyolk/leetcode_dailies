# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    """1260. Shift 2D Grid
    
    Given a 2D grid of size m x n and an integer k. You need to shift the grid k
    times. In one shift operation: Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0]. Element at grid[m - 1][n -
    1] moves to grid[0][0]. Return the 2D grid after applying shift operation k
    times.
    """
    def shift_grid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        if not grid or not grid[0]:
            return grid
        m = len(grid)
        n = len(grid[0])
        total = m * n
        # reduce k to minimum effective shifts
        k %= total
        if k == 0:
            return [row[:] for row in grid]
        new_grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # current new position in flattened array
                pos = i * n + j
                # source position before k right shifts
                old_pos = (pos - k) % total
                old_i = old_pos // n
                old_j = old_pos % n
                new_grid[i][j] = grid[old_i][old_j]
        return new_grid

    shiftGrid = shift_grid
