# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/


class Solution:
    """1685. Sum of Absolute Differences in a Sorted Array

    You are given an integer array `nums` sorted in **non-decreasing** order.

    Build and return *an integer array* `result` *with the same length as* `nums` *such
    that* `result[i]` *is equal to the **summation of absolute differences** between*
    `nums[i]` *and all the other elements in the array.*

    In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where `0 <= j <
    nums.length` and `j != i` (**0-indexed**).
    """

    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        ...

    getSumAbsoluteDifferences = get_sum_absolute_differences
