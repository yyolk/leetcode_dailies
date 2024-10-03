# https://leetcode.com/problems/make-sum-divisible-by-p/


class Solution:
    """1590. Make Sum Divisible by P

    Given an array of positive integers `nums`, remove the **smallest** subarray
    (possibly **empty**) such that the **sum** of the remaining elements is divisible by
    `p`. It is **not** allowed to remove the whole array.

    Return *the length of the smallest subarray that you need to remove, or* `-1` *if
    it's impossible*.

    A **subarray** is defined as a contiguous block of elements in the array.

    """

    def min_subarray(self, nums: list[int], p: int) -> int: ...

    minSubarray = min_subarray
