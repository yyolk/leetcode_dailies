# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution:
    """2444. Count Subarrays With Fixed Bounds

    You are given an integer array `nums` and two integers `min_k` and `max_k`.

    A **fixed-bound subarray** of `nums` is a subarray that satisfies the following
    conditions:

    * The **minimum** value in the subarray is equal to `min_k`.

    * The **maximum** value in the subarray is equal to `max_k`.

    Return *the **number** of fixed-bound subarrays*.

    A **subarray** is a **contiguous** part of an array."""

    def count_subarrays(self, nums: list[int], min_k: int, max_k: int) -> int: ...

    countSubarrays = count_subarrays
