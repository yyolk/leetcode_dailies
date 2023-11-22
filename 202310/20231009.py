# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    """34. Find First and Last Position of Element in Sorted Array

    Given an array of integers `nums` sorted in non-decreasing order, find the starting and
    ending position of a given `target` value.

    If `target` is not found in the array, return `[-1, -1]`.

    You must write an algorithm with `O(log n)` runtime complexity.
    """

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """Search the input nums list of int for the target element.

        Proposed solution using a modified binary search approach.

        Args:
            nums (list of int): Input nums to search for target.
            target (int): Input target int to search for in nums.

        Returns:
            list of int: The starting and ending index of the found target int
            found within the input nums.
        """

        def find_left(nums: list[int], target: int) -> int:
            """Helper function to find the leftmost occurence of the target"""
            left, right = 0, len(nums) - 1
            while left <= right:
                # Calculate the middle index
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # If the target is found, narrow the search to the left half
                    right = mid - 1
                elif nums[mid] < target:
                    # If the target is greater, search the right half
                    left = mid + 1
                else:
                    # If the target is smaller, search the left half
                    right = mid - 1
            return left

        def find_right(nums: list[int], target: int) -> int:
            """Helper funciton to find the rightmost occurence of the target"""
            left, right = 0, len(nums) - 1
            while left <= right:
                # Calculate the middle index
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # If target found, narrow the search to the right half
                    left = mid + 1
                elif nums[mid] < target:
                    # If the target is greater, search the right half
                    left = mid + 1
                else:
                    # If the target is smaller, search the left half
                    right = mid - 1
            return right

        # Call helper functions to find left and right indices
        left_index = find_left(nums, target)
        right_index = find_right(nums, target)

        # Check if a valid range is found
        if left_index <= right_index:
            # Return the range
            return [left_index, right_index]
        else:
            # Target is not found, return [-1, -1]
            return [-1, -1]
