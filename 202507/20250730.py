# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/


class Solution:
    """2419. Longest Subarray With Maximum Bitwise AND

    You are given an integer array `nums` of size `n`.

    Consider a **non-empty** subarray from `nums` that has the **maximum** possible
    **bitwise AND**.

    * In other words, let `k` be the maximum value of the bitwise AND of **any**
    subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be
    considered.

    Return *the length of the **longest** such subarray*.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A **subarray** is a contiguous sequence of elements within an array."""

    def longest_subarray(self, nums: list[int]) -> int: ...

    longestSubarray = longest_subarray
