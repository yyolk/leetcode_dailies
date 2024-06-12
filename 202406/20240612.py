# https://leetcode.com/problems/sort-colors/


class Solution:
    """75. Sort Colors

    Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-
    place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the
    same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers `0`, `1`, and `2` to represent the color red, white, and
    blue, respectively.

    You must solve this problem without using the library's sort function.

    """

    def sort_colors(self, nums: list[int]) -> None:
        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse through the list
        while mid <= high:
            if nums[mid] == 0:
                # If the current element is 0, swap it with the element at low pointer
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If the current element is 1, move the mid pointer
                mid += 1
            else:
                # If the current element is 2, swap it with the element at high pointer
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
    
    sortColors = sort_colors
