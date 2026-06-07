# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/


class Solution:
    """2134. Minimum Swaps to Group All 1's Together II

    A **swap** is defined as taking two **distinct** positions in an array and swapping
    the values in them.

    A **circular** array is defined as an array where we consider the **first** element
    and the **last** element to be **adjacent**.

    Given a **binary** **circular** array `nums`, return *the minimum number of swaps
    required to group all* `1`*'s present in the array together at **any location***.

    """

    def min_swaps(self, nums: list[int]) -> int:
        # Count the total number of 1's in the array
        total_ones = sum(nums)

        # If there are no 1's or all elements are 1's, no swaps are needed
        if total_ones == 0 or total_ones == len(nums):
            return 0

        # To handle the circular nature, we extend the array by itself
        nums = nums + nums

        # Initialize variables for the sliding window
        current_zeros = 0
        min_swaps = float("inf")

        # Initial window of size total_ones
        for i in range(total_ones):
            if nums[i] == 0:
                current_zeros += 1

        # Set the initial number of zeros as the minimum swaps
        min_swaps = current_zeros

        # Slide the window across the array
        for i in range(1, len(nums) - total_ones + 1):
            # Remove the influence of the outgoing element from the window
            if nums[i - 1] == 0:
                current_zeros -= 1
            # Add the influence of the incoming element to the window
            if nums[i + total_ones - 1] == 0:
                current_zeros += 1
            # Update the minimum number of zeros found in any window
            min_swaps = min(min_swaps, current_zeros)

        return min_swaps

    minSwaps = min_swaps
