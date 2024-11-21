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
    ) -> int: ...

    countUnguarded = count_unguarded
