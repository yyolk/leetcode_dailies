# https://leetcode.com/problems/zero-array-transformation-i/


class Solution:
    """3355. Zero Array Transformation I

    You are given an integer array `nums` of length `n` and a 2D array `queries`, where
    `queries[i] = [li, ri]`.

    For each `queries[i]`:

    * Select a subset of indices within the range `[li, ri]` in `nums`.

    * Decrement the values at the selected indices by 1.

    A **Zero Array** is an array where all elements are equal to 0.

    Return `true` if it is *possible* to transform `nums` into a **Zero Array** after
    processing all the queries sequentially, otherwise return `false`."""

    def is_zero_array(self, nums: list[int], queries: list[list[int]]) -> bool: ...

    isZeroArray = is_zero_array
