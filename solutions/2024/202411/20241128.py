# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
from collections import deque


class Solution:
    """2290. Minimum Obstacle Removal to Reach Corner

    You are given a **0-indexed** 2D integer array `grid` of size `m x n`. Each cell has
    one of two values:

    * `0` represents an **empty** cell,

    * `1` represents an **obstacle** that may be removed.

    You can move up, down, left, or right from and to an empty cell.

    Return *the **minimum** number of **obstacles** to **remove** so you can move from
    the upper left corner* `(0, 0)` *to the lower right corner* `(m - 1, n - 1)`."""

    def minimum_obstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        # (x, y, obstacles_removed)
        queue = deque([(0, 0, 0)])

        while queue:
            x, y, obstacles = queue.popleft()
            if x == m - 1 and y == n - 1:
                return obstacles

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    # obstacle
                    if grid[nx][ny] == 1:
                        queue.append((nx, ny, obstacles + 1))
                    else:
                        # no need to remove obstacle
                        queue.appendleft((nx, ny, obstacles))

        # If there's no path to the destination
        return -1

    minimumObstacles = minimum_obstacles
