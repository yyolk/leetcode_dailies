# https://leetcode.com/problems/minimum-falling-path-sum-ii/


class Solution:
    """1289. Minimum Falling Path Sum II

    Given an `n x n` integer matrix `grid`, return *the minimum sum of a **falling path
    with non-zero shifts***.

    A **falling path with non-zero shifts** is a choice of exactly one element from each
    row of `grid` such that no two elements chosen in adjacent rows are in the same
    column.

    """

    def min_falling_path_sum(self, grid: list[list[int]]) -> int: ...

    minFallingPathSum = min_falling_path_sum
