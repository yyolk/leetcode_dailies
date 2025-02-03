# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/


class Solution:
    """3105. Longest Strictly Increasing or Strictly Decreasing Subarray

    You are given an array of integers `nums`. Return *the length of the **longest**
    subarray of* `nums` *which is either **strictly increasing** or **strictly
    decreasing***."""

    def longest_monotonic_subarray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1
        current_inc_length = 1
        current_dec_length = 1
        
        for i in range(1, len(nums)):
            # Use match to compare nums[i] and nums[i - 1]
            match (nums[i], nums[i - 1]):
                case (x, y) if x > y:
                    current_inc_length += 1
                    current_dec_length = 1
                case (x, y) if x < y:
                    current_dec_length += 1
                    current_inc_length = 1
                case _:
                    current_inc_length = 1
                    current_dec_length = 1
            
            max_length = max(max_length, current_inc_length, current_dec_length)
        
        return max_length

    longestMonotonicSubarray = longest_monotonic_subarray
