# https://leetcode.com/problems/continuous-subarrays/
from collections import deque


class Solution:
    """2762. Continuous Subarrays

    You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called
    **continuous** if:

    * Let `i`, `i + 1`, ..., `j`be the indices in the subarray. Then, for each pair of
    indices `i <= i1, i2 <= j`, `0 <= |nums[i1] - nums[i2]| <= 2`.

    Return *the total number of **continuous** subarrays.*

    A subarray is a contiguous **non-empty** sequence of elements within an array."""

    def continuous_subarrays(self, nums: list[int]) -> int:
        # Initialize left pointer of the window
        left_pointer = 0
        # Initialize result counter
        result_count = 0

        # Deque for minimum values in the current window
        minimum_deque = deque()
        # Deque for maximum values in the current window
        maximum_deque = deque()

        # Iterate through each element in nums
        for right_pointer in range(len(nums)):
            # Remove indices from the back of minimum_deque if their values are greater than or equal to current number
            while minimum_deque and nums[minimum_deque[-1]] >= nums[right_pointer]:
                minimum_deque.pop()
            # Remove indices from the back of maximum_deque if their values are less than or equal to current number
            while maximum_deque and nums[maximum_deque[-1]] <= nums[right_pointer]:
                maximum_deque.pop()
            # Add current index to minimum_deque
            minimum_deque.append(right_pointer)
            # Add current index to maximum_deque
            maximum_deque.append(right_pointer)

            # Adjust the window if the difference between max and min exceeds 2
            while nums[maximum_deque[0]] - nums[minimum_deque[0]] > 2:
                left_pointer += 1
                # Remove the left pointer from minimum_deque if it's no longer in the window
                if minimum_deque[0] < left_pointer:
                    minimum_deque.popleft()
                # Remove the left pointer from maximum_deque if it's no longer in the window
                if maximum_deque[0] < left_pointer:
                    maximum_deque.popleft()

            # Count the number of continuous subarrays ending at right_pointer
            result_count += right_pointer - left_pointer + 1

        # Return the total count of continuous subarrays
        return result_count

    continuousSubarrays = continuous_subarrays
