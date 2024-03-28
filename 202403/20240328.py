# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/


class Solution:
    """2958. Length of Longest Subarray With at Most K Frequency

    You are given an integer array `nums` and an integer `k`.

    The **frequency** of an element `x` is the number of times it occurs in an array.

    An array is called **good** if the frequency of each element in this array is **less
    than or equal** to `k`.

    Return *the length of the **longest** **good** subarray of* `nums`*.*

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    """

    def max_subarray_length(self, nums: list[int], k: int) -> int:
        # Dictionary to keep track of the frequency of each number in nums
        frequency_map = {}
        # Pointer to the starting index of the current subarray
        left = 0
        # The maximum length of a good subarray found so far
        max_length = 0

        # Iterate through the nums array
        for right, num in enumerate(nums):
            # If the current number is not in the frequency map, add it
            if num not in frequency_map:
                frequency_map[num] = 0
            # Increment the frequency of the current number
            frequency_map[num] += 1

            # If the frequency of the current number is greater than k
            while frequency_map[num] > k:
                # Decrement the frequency of the element at the left pointer
                frequency_map[nums[left]] -= 1
                # If the frequency becomes 0, remove it from the frequency map
                if frequency_map[nums[left]] == 0:
                    del frequency_map[nums[left]]
                # Move the left pointer to the right
                left += 1

            # Update the maximum length of a good subarray
            max_length = max(max_length, right - left + 1)

        return max_length

    maxSubarrayLength = max_subarray_length

