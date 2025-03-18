# https://leetcode.com/problems/longest-nice-subarray/


class Solution:
    """2401. Longest Nice Subarray

    You are given an array `nums` consisting of **positive** integers.

    We call a subarray of `nums` **nice** if the bitwise **AND** of every pair of
    elements that are in **different** positions in the subarray is equal to `0`.

    Return *the length of the **longest** nice subarray*.

    A **subarray** is a **contiguous** part of an array.

    **Note** that subarrays of length `1` are always considered nice."""

    def longest_nice_subarray(self, nums: list[int]) -> int: ...

    longestNiceSubarray = longest_nice_subarray
