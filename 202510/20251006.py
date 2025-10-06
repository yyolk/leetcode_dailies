# https://leetcode.com/problems/swim-in-rising-water/


class Solution:
    """778. Swim in Rising Water

    You are given an `n x n` integer matrix `grid` where each value `grid[i][j]`
    represents the elevation at that point `(i, j)`.

    It starts raining, and water gradually rises over time. At time `t`, the water level
    is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or
    reachable.

    You can swim from a square to another 4-directionally adjacent square if and only if
    the elevation of both squares individually are at most `t`. You can swim infinite
    distances in zero time. Of course, you must stay within the boundaries of the grid
    during your swim.

    Return *the minimum time until you can reach the bottom right square* `(n - 1, n -
    1)` *if you start at the top left square* `(0, 0)`."""

    def swim_in_water(self, grid: list[list[int]]) -> int: ...

    swimInWater = swim_in_water
