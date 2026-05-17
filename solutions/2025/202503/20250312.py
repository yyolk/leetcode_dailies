# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
import bisect


class Solution:
    """2529. Maximum Count of Positive Integer and Negative Integer

    Given an array `nums` sorted in **non-decreasing** order, return *the maximum
    between the number of positive integers and the number of negative integers.*

    * In other words, if the number of positive integers in `nums` is `pos` and the
    number of negative integers is `neg`, then return the maximum of `pos` and `neg`.

    **Note** that `0` is neither positive nor negative."""

    def maximum_count(self, nums: list[int]) -> int:
        # Count of negative numbers: index of first element >= 0
        neg_count = bisect.bisect_left(nums, 0)
        # Count of positive numbers: total length minus index of first element > 0
        pos_count = len(nums) - bisect.bisect_right(nums, 0)
        # Return the maximum of the two counts
        return max(neg_count, pos_count)

    maximumCount = maximum_count
