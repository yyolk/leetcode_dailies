# https://leetcode.com/problems/sort-colors/


class Solution:
    """75. Sort Colors

    Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-
    place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the
    same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers `0`, `1`, and `2` to represent the color red, white, and
    blue, respectively.

    You must solve this problem without using the library's sort function."""

    def sort_colors(self, nums: list[int]):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

    sortColors = sort_colors
