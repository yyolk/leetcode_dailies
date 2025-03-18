# https://leetcode.com/problems/longest-nice-subarray/


class Solution:
    """2401. Longest Nice Subarray

    You are given an array `nums` consisting of **positive** integers.

    We call a subarray of `nums` **nice** if the bitwise **AND** of every pair of
    elements that are in **different** positions in the subarray is equal to `0`.

    Return *the length of the **longest** nice subarray*.

    A **subarray** is a **contiguous** part of an array.

    **Note** that subarrays of length `1` are always considered nice."""

    def longest_nice_subarray(self, nums: list[int]) -> int:
        # Initialize the maximum length of the nice subarray to 1 (minimum possible)
        max_len = 1
        # Get the number of elements in the input list
        n = len(nums)
        # Iterate over each possible starting index of the subarray
        for i in range(n):
            # Initialize current_or to accumulate the OR of elements in the current window
            current_or = 0
            # Check the next 30 elements or until the end of the array
            for j in range(i, min(i + 30, n)):
                # If the current element AND with current_or is non-zero, conflict found
                if nums[j] & current_or != 0:
                    # Break the inner loop as further elements can't form a valid subarray starting at i
                    break
                # Update current_or by including the current element's bits
                current_or |= nums[j]
                # Calculate the current subarray length
                current_length = j - i + 1
                # Update max_len if current_length is greater
                if current_length > max_len:
                    max_len = current_length
        # Return the maximum length found
        return max_len

    longestNiceSubarray = longest_nice_subarray
