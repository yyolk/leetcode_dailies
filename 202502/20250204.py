# https://leetcode.com/problems/maximum-ascending-subarray-sum/


class Solution:
    """1800. Maximum Ascending Subarray Sum

    Given an array of positive integers `nums`, return the *maximum possible sum of an
    **ascending** subarray in* `nums`.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is **ascending** if for all `i`
    where `l <= i < r`, `numsi  < numsi+1`. Note that a subarray of size `1` is
    **ascending**."""

    def max_ascending_sum(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum

    maxAscendingSum = max_ascending_sum
