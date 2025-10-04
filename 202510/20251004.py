# https://leetcode.com/problems/container-with-most-water/


class Solution:
    """11. Container With Most Water

    You are given an integer array `height` of length `n`. There are `n` vertical lines
    drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i,
    height[i])`.

    Find two lines that together with the x-axis form a container, such that the
    container contains the most water.

    Return *the maximum amount of water a container can store*.

    **Notice** that you may not slant the container."""

    def max_area(self, height: list[int]) -> int:
        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(height) - 1
        # Initialize the maximum area found so far
        max_area = 0
        # Continue until the pointers meet
        while left < right:
            # Calculate the area between the current pointers
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            # Move the pointer with the smaller height inward to potentially increase area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Return the maximum area after checking all possible containers
        return max_area

    maxArea = max_area
