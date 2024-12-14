# https://leetcode.com/problems/continuous-subarrays/


class Solution:
    """2762. Continuous Subarrays

    You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called
    **continuous** if:

    * Let `i`, `i + 1`, ..., `j`be the indices in the subarray. Then, for each pair of
    indices `i <= i1, i2 <= j`, `0 <= |nums[i1] - nums[i2]| <= 2`.

    Return *the total number of **continuous** subarrays.*

    A subarray is a contiguous **non-empty** sequence of elements within an array."""

    def continuous_subarrays(self, nums: list[int]) -> int: ...

    continuousSubarrays = continuous_subarrays
