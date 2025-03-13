# https://leetcode.com/problems/zero-array-transformation-ii/


class Solution:
    """3356. Zero Array Transformation II

    You are given an integer array `nums` of length `n` and a 2D array `queries` where
    `queries[i] = [li, ri, vali]`.

    Each `queries[i]` represents the following action on `nums`:

    * Decrement the value at each index in the range `[li, ri]` in `nums` by **at most**
    `vali`.

    * The amount by which each value is decremented can be chosen **independently** for
    each index.

    A **Zero Array** is an array with all its elements equal to 0.

    Return the **minimum** possible **non-negative** value of `k`, such that after
    processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**.
    If no such `k` exists, return -1."""

    def min_zero_array(self, nums: list[int], queries: list[list[int]]) -> int: ...

    minZeroArray = min_zero_array
