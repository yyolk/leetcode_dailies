# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
from math import ceil


class Solution:
    """1760. Minimum Limit of Balls in a Bag

    You are given an integer array `nums` where the `ith` bag contains `nums[i]` balls.
    You are also given an integer `max_operations`.

    You can perform the following operation at most `max_operations` times:

    * Take any bag of balls and divide it into two new bags with a **positive** number
    of balls.

      + For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or
    two new bags of `2` and `3` balls.

    Your penalty is the **maximum** number of balls in a bag. You want to **minimize**
    your penalty after the operations.

    Return *the minimum possible penalty after performing the operations*."""

    def minimum_size(self, nums: list[int], max_operations: int) -> int:
        # Define a helper function to check if a given penalty is achievable
        def can_be_penalty(penalty: int) -> bool:
            # Initialize operation counter
            operations = 0
            # Iterate through each number in nums
            for num in nums:
                # Calculate operations needed for current number with given penalty
                operations += (num - 1) // penalty  # ceil(num / penalty) - 1
            # Check if total operations do not exceed max_operations
            return operations <= max_operations

        # Set the lower bound of binary search to 1
        left, right = 1, max(nums)
        
        # Perform binary search to find the minimum penalty
        while left < right:
            # Calculate midpoint for binary search
            mid = (left + right) // 2
            # If mid is a valid penalty, try a lower penalty
            if can_be_penalty(mid):
                right = mid
            # If mid is not valid, we need to increase the penalty
            else:
                left = mid + 1
        
        # Return the minimum penalty found
        return left

    minimumSize = minimum_size
