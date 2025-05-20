# https://leetcode.com/problems/zero-array-transformation-i/


class Solution:
    """3355. Zero Array Transformation I

    You are given an integer array `nums` of length `n` and a 2D array `queries`, where
    `queries[i] = [li, ri]`.

    For each `queries[i]`:

    * Select a subset of indices within the range `[li, ri]` in `nums`.

    * Decrement the values at the selected indices by 1.

    A **Zero Array** is an array where all elements are equal to 0.

    Return `true` if it is *possible* to transform `nums` into a **Zero Array** after
    processing all the queries sequentially, otherwise return `false`."""

    def is_zero_array(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        
        # Step 1: Check if any element in nums is negative
        if any(num < 0 for num in nums):
            return False
        
        # Step 2: Initialize cover array to track query coverage using difference array technique
        cover = [0] * (n + 1)
        for li, ri in queries:
            cover[li] += 1
            if ri + 1 < n:
                cover[ri + 1] -= 1
        
        # Step 3: Compute prefix sum and check feasibility
        current = 0
        for i in range(n):
            current += cover[i]
            if nums[i] > current:
                return False
        
        return True

    isZeroArray = is_zero_array
