# https://leetcode.com/problems/count-the-number-of-good-subarrays/


class Solution:
    """2537. Count the Number of Good Subarrays

    Given an integer array `nums` and an integer `k`, return *the number of **good**
    subarrays of* `nums`.

    A subarray `arr` is **good** if there are **at least** `k` pairs of indices `(i, j)`
    such that `i < j` and `arr[i] == arr[j]`.

    A **subarray** is a contiguous **non-empty** sequence of elements within an array.
    """

    def count_good(self, nums: list[int], k: int) -> int: ...

    countGood = count_good
