# https://leetcode.com/problems/minimum-distance-to-the-target-element

class Solution:
    """1848. Minimum Distance to the Target Element
    
    Given an integer array nums (0-indexed) and two integers target and
    start, find an index i such that nums[i] == target and abs(i - start) is
    minimized. Note that abs(x) is the absolute value of x.
    
    Return abs(i - start).
    It is guaranteed that target exists in nums.
    """
    def get_min_distance(self, nums: list[int], target: int, start: int) -> int:
        # Track the smallest distance seen so far
        min_dist = float("inf")
        # Single pass to check every position
        for i in range(len(nums)):
            if nums[i] == target:
                # Update minimum with absolute distance to start
                min_dist = min(min_dist, abs(i - start))
        return min_dist

    getMinDistance = get_min_distance