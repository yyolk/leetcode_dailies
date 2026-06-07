# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/


class Solution:
    """3487. Maximum Unique Subarray Sum After Deletion

    You are given an integer array `nums`.

    You are allowed to delete any number of elements from `nums` without making it
    **empty**. After performing the deletions, select a subarray of `nums` such that:

    1. All elements in the subarray are **unique**.

    2. The sum of the elements in the subarray is **maximized**.

    Return the **maximum sum** of such a subarray."""

    def max_sum(self, nums: list[int]) -> int:
        # Create a set of unique elements from the input array
        unique = set(nums)
        # Calculate the sum of positive unique elements
        pos_sum = sum(x for x in unique if x > 0)
        # Return the positive sum if it's greater than 0, otherwise return the maximum element
        return pos_sum if pos_sum > 0 else max(nums)

    maxSum = max_sum
