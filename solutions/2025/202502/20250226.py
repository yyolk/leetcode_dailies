# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/


class Solution:
    """1749. Maximum Absolute Sum of Any Subarray

    You are given an integer array `nums`. The **absolute sum** of a subarray `[numsl,
    numsl+1, ..., numsr-1, numsr]` is `abs(numsl + numsl+1 + ... + numsr-1 + numsr)`.

    Return *the **maximum** absolute sum of any **(possibly empty)** subarray of*
    `nums`.

    Note that `abs(x)` is defined as follows:

    * If `x` is a negative integer, then `abs(x) = -x`.

    * If `x` is a non-negative integer, then `abs(x) = x`."""

    def max_absolute_sum(self, nums: list[int]) -> int:
        # Initialize variables with the first element
        max_ending_here = min_ending_here = nums[0]
        max_so_far = min_so_far = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update maximum sum ending at current position
            max_ending_here = max(num, max_ending_here + num)
            # Update minimum sum ending at current position
            min_ending_here = min(num, min_ending_here + num)
            # Update global maximum subarray sum
            max_so_far = max(max_so_far, max_ending_here)
            # Update global minimum subarray sum
            min_so_far = min(min_so_far, min_ending_here)

        # Return the maximum absolute sum, considering empty subarray (sum 0)
        return max(0, max_so_far, -min_so_far)

    maxAbsoluteSum = max_absolute_sum
