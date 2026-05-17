# https://leetcode.com/problems/number-of-zero-filled-subarrays/


class Solution:
    """2348. Number of Zero-Filled Subarrays

    Given an integer array `nums`, return *the number of **subarrays** filled with* `0`.

    A **subarray** is a contiguous non-empty sequence of elements within an array."""

    def zero_filled_subarray(self, nums: list[int]) -> int:
        # Initialize total count of zero-filled subarrays
        total = 0
        # Track current streak of consecutive zeros
        streak = 0
        for num in nums:
            if num == 0:
                # Increment streak for current zero
                streak += 1
                # Add the number of new subarrays ending at this position
                total += streak
            else:
                # Reset streak when non-zero is encountered
                streak = 0
        # Return the accumulated total
        return total

    zeroFilledSubarray = zero_filled_subarray
