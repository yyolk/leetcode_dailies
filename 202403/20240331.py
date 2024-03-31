# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution:
    """2444. Count Subarrays With Fixed Bounds

    You are given an integer array `nums` and two integers `min_k` and `max_k`.

    A **fixed-bound subarray** of `nums` is a subarray that satisfies the following
    conditions:

    * The **minimum** value in the subarray is equal to `min_k`.

    * The **maximum** value in the subarray is equal to `max_k`.

    Return *the **number** of fixed-bound subarrays*.

    A **subarray** is a **contiguous** part of an array.

    """

    def count_subarrays(self, nums: list[int], min_k: int, max_k: int) -> int:
        # Initialize the result counter
        res = 0

        # Initialize indices for tracking invalid numbers and bounds
        bad_idx = left_idx = right_idx = -1

        # Iterate through the input array
        for i, num in enumerate(nums):
            # If the current number is outside the bounds
            if not min_k <= num <= max_k:
                # Set the index of the invalid number
                bad_idx = i

            # If the current number is the minimum bound
            if num == min_k:
                # Set the index of the minimum bound
                left_idx = i

            # If the current number is the maximum bound
            if num == max_k:
                # Set the index of the maximum bound
                right_idx = i

            # Add the count of valid subarrays to the result
            res += max(0, min(left_idx, right_idx) - bad_idx)

        # Return the final result
        return res


    countSubarrays = count_subarrays
