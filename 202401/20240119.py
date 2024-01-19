# https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    """931. Minimum Falling Path Sum

    Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any
    **falling path** through* `matrix`.

    A **falling path** starts at any element in the first row and chooses the element in
    the next row that is either directly below or diagonally left/right. Specifically,
    the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1,
    col)`, or `(row + 1, col + 1)`.
    """

    def min_falling_path_sum(self, matrix: list[list[int]]) -> int:
        ...

    minFallingPathSum = min_falling_path_sum
