# https://leetcode.com/problems/map-of-highest-peak/
from collections import deque


class Solution:
    """1765. Map of Highest Peak

    You are given an integer matrix `is_water` of size `m x n` that represents a map of
    **land** and **water** cells.

    * If `is_water[i][j] == 0`, cell `(i, j)` is a **land** cell.

    * If `is_water[i][j] == 1`, cell `(i, j)` is a **water** cell.

    You must assign each cell a height in a way that follows these rules:

    * The height of each cell must be non-negative.

    * If the cell is a **water** cell, its height must be `0`.

    * Any two adjacent cells must have an absolute height difference of **at most** `1`.
    A cell is adjacent to another cell if the former is directly north, east, south, or
    west of the latter (i.e., their sides are touching).

    Find an assignment of heights such that the maximum height in the matrix is
    **maximized**.

    Return *an integer matrix* `height` *of size* `m x n` *where* `height[i][j]` *is
    cell* `(i, j)`*'s height. If there are multiple solutions, return **any** of them*.
    """

    def highest_peak(self, is_water: list[list[int]]) -> list[list[int]]:
        m, n = len(is_water), len(is_water[0])
        height = [[-1] * n for _ in range(m)]
        queue = deque()

        # Initialize water cells
        for i in range(m):
            for j in range(n):
                # Water cell
                if is_water[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        # BFS from water cells to land cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))

        return height

    highestPeak = highest_peak
