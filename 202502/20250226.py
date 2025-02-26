# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/


class Solution:
    """1749. Maximum Absolute Sum of Any Subarray

    You are given an integer array `nums`. The **absolute sum** of a subarray `[numsl,
    numsl+1, ..., numsr-1, numsr]` is `abs(numsl + numsl+1 + ... + numsr-1 + numsr)`.

    Return *the **maximum** absolute sum of any **(possibly empty)** subarray of*
    `nums`.

    Note that `abs(x)` is defined as follows:

    * If `x` is a negative integer, then `abs(x) = -x`.

    * If `x` is a non-negative integer, then `abs(x) = x`."""

    def max_absolute_sum(self, nums: list[int]) -> int: ...

    maxAbsoluteSum = max_absolute_sum
