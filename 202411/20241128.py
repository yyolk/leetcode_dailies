# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/


class Solution:
    """2290. Minimum Obstacle Removal to Reach Corner

    You are given a **0-indexed** 2D integer array `grid` of size `m x n`. Each cell has
    one of two values:

    * `0` represents an **empty** cell,

    * `1` represents an **obstacle** that may be removed.

    You can move up, down, left, or right from and to an empty cell.

    Return *the **minimum** number of **obstacles** to **remove** so you can move from
    the upper left corner* `(0, 0)` *to the lower right corner* `(m - 1, n - 1)`."""

    def minimum_obstacles(self, grid: list[list[int]]) -> int: ...

    minimumObstacles = minimum_obstacles
