# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/


class Solution:
    """3396. Minimum Number of Operations to Make Elements in Array Distinct

    You are given an integer array `nums`. You need to ensure that the elements in the
    array are **distinct**. To achieve this, you can perform the following operation any
    number of times:

    * Remove 3 elements from the beginning of the array. If the array has fewer than 3
    elements, remove all remaining elements.

    **Note** that an empty array is considered to have distinct elements. Return the
    **minimum** number of operations needed to make the elements in the array distinct.
    """

    def minimum_operations(self, nums: list[int]) -> int:
        # Store the length of the array for easier reference
        n = len(nums)
        # Initialize the operation counter to track the number of removals
        k = 0
        # Loop until we find the smallest number of operations to make the suffix distinct
        while True:
            # Extract the suffix after removing the first 3*k elements
            suffix = nums[3 * k :]
            # Check if the suffix has all distinct elements by comparing set length to list length
            if len(set(suffix)) == len(suffix):
                # If suffix is distinct (or empty), return the number of operations performed
                return k
            # If suffix has duplicates, increment k to remove more elements in the next iteration
            k += 1

    minimumOperations = minimum_operations
