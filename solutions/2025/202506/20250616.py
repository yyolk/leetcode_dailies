# https://leetcode.com/problems/maximum-difference-between-increasing-elements/


class Solution:
    """2016. Maximum Difference Between Increasing Elements

    Given a **0-indexed** integer array `nums` of size `n`, find the **maximum
    difference** between `nums[i]` and `nums[j]` (i.e., `nums[j] - nums[i]`), such that
    `0 <= i < j < n` and `nums[i] < nums[j]`.

    Return *the **maximum difference**.* If no such `i` and `j` exists, return `-1`."""

    def maximum_difference(self, nums: list[int]) -> int:
        # Initialize the minimum value seen so far and maximum difference
        min_so_far = nums[0]
        max_diff = -1

        # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            # If current element is greater than the minimum so far
            if nums[j] > min_so_far:
                # Calculate the difference and update max_diff if larger
                max_diff = max(max_diff, nums[j] - min_so_far)
            # Update the minimum value seen so far
            min_so_far = min(min_so_far, nums[j])

        return max_diff

    maximumDifference = maximum_difference
