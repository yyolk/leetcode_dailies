# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/


class Solution:
    """2873. Maximum Value of an Ordered Triplet I

    You are given a **0-indexed** integer array `nums`.

    Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that*
    `i < j < k`. If all such triplets have a negative value, return `0`.

    The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) *
    nums[k]`."""

    def maximum_triplet_value(self, nums: list[int]) -> int: ...

    maximumTripletValue = maximum_triplet_value
