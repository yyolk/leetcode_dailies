# https://leetcode.com/problems/patching-array/


class Solution:
    """330. Patching Array

    Given a sorted integer array `nums` and an integer `n`, add/patch elements to the
    array such that any number in the range `[1, n]` inclusive can be formed by the sum
    of some elements in the array.

    Return *the minimum number of patches required*.

    """

    def min_patches(self, nums: list[int], n: int) -> int:
        patches = 0
        i = 0
        current_sum = 1
        
        # Loop until we can form all numbers in the range [1, n]
        while current_sum <= n:
            if i < len(nums) and nums[i] <= current_sum:
                # If the current number in nums can extend the range
                current_sum += nums[i]
                i += 1
            else:
                # If the current number in nums cannot extend the range
                # Patch the array by adding current_sum
                current_sum += current_sum
                patches += 1
        
        return patches

    minPatches = min_patches
