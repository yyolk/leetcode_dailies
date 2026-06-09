# https://leetcode.com/problems/maximum-total-subarray-value-i/


class Solution:
    """3689. Maximum Total Subarray Value I

    You are given an integer array `nums` of length `n` and an integer `k`.

    You need to choose **exactly** `k` non-empty subarrays `nums[l..r]` of `nums`.
    Subarrays may overlap, and the exact same subarray (same `l` and `r`) **can** be
    chosen more than once.

    The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) -
    min(nums[l..r])`.

    The **total value** is the sum of the **values** of all chosen subarrays.

    Return the **maximum** possible total value you can achieve."""

    def max_total_value(self, nums: list[int], k: int) -> int: ...

    maxTotalValue = max_total_value
