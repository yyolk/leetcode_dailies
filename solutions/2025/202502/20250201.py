# https://leetcode.com/problems/special-array-i/
from itertools import pairwise


class Solution:
    """3151. Special Array I

    An array is considered **special** if every pair of its adjacent elements contains
    two numbers with different parity.

    You are given an array of integers `nums`. Return `true` if `nums` is a **special**
    array, otherwise, return `false`."""

    def is_array_special(self, nums: list[int]) -> bool:
        # Use pairwise to check parity of adjacent elements
        for a, b in pairwise(nums):
            # If parity is the same, array is not special
            if (a % 2) == (b % 2):
                return False
        return True

    isArraySpecial = is_array_special
