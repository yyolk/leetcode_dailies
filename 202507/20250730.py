# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/


class Solution:
    """2419. Longest Subarray With Maximum Bitwise AND

    You are given an integer array `nums` of size `n`.

    Consider a **non-empty** subarray from `nums` that has the **maximum** possible
    **bitwise AND**.

    * In other words, let `k` be the maximum value of the bitwise AND of **any**
    subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be
    considered.

    Return *the length of the **longest** such subarray*.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A **subarray** is a contiguous sequence of elements within an array."""

    def longest_subarray(self, nums: list[int]) -> int:
        # Check if the input array is empty
        if not nums:
            # Return 0 for empty array
            return 0
        # Find the maximum value in the array, as bitwise AND cannot exceed this
        m = max(nums)
        # Initialize variable to store the maximum length of subarray
        ans = 0
        # Initialize variable to track current streak of maximum values
        curr = 0
        # Iterate through each number in the array
        for x in nums:
            # Check if current number equals the maximum value
            if x == m:
                # Increment current streak
                curr += 1
                # Update maximum length if current streak is longer
                ans = max(ans, curr)
            else:
                # Reset current streak if number is not maximum
                curr = 0
        # Return the length of the longest subarray
        return ans

    longestSubarray = longest_subarray
