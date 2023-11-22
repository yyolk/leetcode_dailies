# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
import sys

from bisect import bisect_right


class Solution:
    """2009. Minimum Number of Operations to Make Array Continuous

    You are given an integer array `nums`. In one operation, you can replace **any**
    element in `nums` with **any** integer.

    `nums` is considered **continuous** if both of the following conditions are
    fulfilled:

    * All elements in `nums` are **unique**.

    * The difference between the **maximum** element and the **minimum** element in
    `nums` equals `nums.length - 1`.

    For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]`
    is **not continuous**.

    Return *the **minimum** number of operations to make* `nums`***continuous***.
    """

    def minOperations(self, nums: list[int]) -> int:
        """The minimum operations to make input nums continuous.

        Proposed solution using bisect module, set, and sorted.

        Args:
            nums (list of int): The input nums to make continuous.

        Returns:
            int: The minimum number of operations to make nums continous.
        """
        # Length of input array
        n = len(nums)

        # Remove duplicates and sort the input
        nums = sorted(set(nums))

        # Initialize with a large value
        min_operations = sys.maxsize

        for i, s in enumerate(nums):
            # Calculate the end of the subarray
            end = s + n - 1

            # Use bisect_right to find the index where end would be inserted
            idx = bisect_right(nums, end)

            # Calculate the minimum number of operations for the subarray
            min_operations = min(min_operations, n - (idx - i))

        # Return the minimum operations
        return min_operations
