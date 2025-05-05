# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    """790. Domino and Tromino Tiling

    You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may
    rotate these shapes.

    ![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

    Given an integer n, return *the number of ways to tile an* `2 x n` *board*. Since
    the answer may be very large, return it **modulo** `109 + 7`.

    In a tiling, every square must be covered by a tile. Two tilings are different if
    and only if there are two 4-directionally adjacent cells on the board such that
    exactly one of the tilings has both squares occupied by a tile."""

    def num_tilings(self, n: int) -> int: ...

    numTilings = num_tilings
