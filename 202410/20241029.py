# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/


class Solution:
    """2684. Maximum Number of Moves in a Grid

    You are given a **0\\-indexed** `m x n` matrix `grid` consisting of **positive**
    integers.

    You can start at **any** cell in the first column of the matrix, and traverse the
    grid in the following way:

    * From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`,
    `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move
    to, should be **strictly** bigger than the value of the current cell.

    Return *the **maximum** number of **moves** that you can perform.*

    """

    def max_moves(self, grid: list[list[int]]) -> int: ...

    maxMoves = max_moves
