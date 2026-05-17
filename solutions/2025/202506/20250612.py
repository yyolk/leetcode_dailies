# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
from itertools import pairwise


class Solution:
    """3423. Maximum Difference Between Adjacent Elements in a Circular Array

    Given a **circular** array `nums`, find the **maximum** absolute difference between
    adjacent elements.

    **Note**: In a circular array, the first and last elements are adjacent."""

    def max_adjacent_distance(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        extended = nums + [nums[0]]
        return max(abs(a - b) for a, b in pairwise(extended))

    maxAdjacentDistance = max_adjacent_distance
