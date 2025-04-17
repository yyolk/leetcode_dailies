# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/


class Solution:
    """2176. Count Equal and Divisible Pairs in an Array

    Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return
    *the **number of pairs*** `(i, j)` *where* `0 <= i < j < n`, *such that* `nums[i] ==
    nums[j]` *and* `(i * j)` *is divisible by* `k`."""

    def count_pairs(self, nums: list[int], k: int) -> int: ...

    countPairs = count_pairs
