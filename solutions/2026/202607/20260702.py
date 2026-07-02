# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

from collections import deque

class Solution:
    """3286. Find a Safe Walk Through a Grid

    You are given an m x n binary matrix grid and an integer health. You start
    on the upper-left corner (0, 0) and would like to get to the lower-right
    corner (m - 1, n - 1). You can move up, down, left, or right to an adjacent
    cell as long as your health remains positive. Cells (i, j) with grid[i][j]
    = 1 are unsafe and reduce your health by 1. Return true if you can reach
    the final cell with health >= 1, else false.
    """
    def find_safe_walk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # deduct for entering start cell (including if unsafe)
        h = health - grid[0][0]
        if h < 1:
            return False
        # max_health[r][c]: highest remaining health reached here
        # prune any inferior (lower health) arrival at same cell
        max_health = [[0] * n for _ in range(m)]
        max_health[0][0] = h
        q = deque([(0, 0, h)])
        while q:
            r, c, h = q.popleft()
            # reached end after deducting its cost and health still >=1
            if r == m - 1 and c == n - 1:
                return True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # deduct upon entering the next cell
                    nh = h - grid[nr][nc]
                    # only enqueue on strictly better health (optimizes speed/memory)
                    if nh >= 1 and nh > max_health[nr][nc]:
                        max_health[nr][nc] = nh
                        q.append((nr, nc, nh))
        return False

    findSafeWalk = find_safe_walk
