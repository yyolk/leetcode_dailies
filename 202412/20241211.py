# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/


class Solution:
    """2779. Maximum Beauty of an Array After Applying Operation

    You are given a **0-indexed** array `nums` and a **non-negative** integer `k`.

    In one operation, you can do the following:

    * Choose an index `i` that **hasn't been chosen before** from the range `[0,
    nums.length - 1]`.

    * Replace `nums[i]` with any integer from the range `[nums[i] - k, nums[i] + k]`.

    The **beauty** of the array is the length of the longest subsequence consisting of
    equal elements.

    Return *the **maximum** possible beauty of the array* `nums` *after applying the
    operation any number of times.*

    **Note** that you can apply the operation to each index **only once**.

    A **subsequence** of an array is a new array generated from the original array by
    deleting some elements (possibly none) without changing the order of the remaining
    elements."""

    def maximum_beauty(self, nums: list[int], k: int) -> int:
        # Sort the array to consider numbers in ascending order
        nums.sort()
        
        # Use two pointers
        left = 0
        right = 0
        max_beauty = 0
        
        while right < len(nums):
            # Check if the difference between current elements is within 2k
            # Since we can increase or decrease by k, the range is nums[right] - nums[left] <= 2k
            while right < len(nums) and nums[right] - nums[left] <= 2 * k:
                right += 1
            
            # The beauty here is the count of numbers within the current window
            max_beauty = max(max_beauty, right - left)
            
            # Move the left pointer for the next window
            left += 1
        
        return max_beauty

    maximumBeauty = maximum_beauty
