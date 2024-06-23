# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
from collections import deque


class Solution:
    """1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

    Given an array of integers `nums` and an integer `limit`, return the size of the
    longest **non-empty** subarray such that the absolute difference between any two
    elements of this subarray is less than or equal to `limit`*.*

    """

    def longest_subarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()  # Will store elements in decreasing order
        min_deque = deque()  # Will store elements in increasing order
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Maintain the decreasing order in max_deque
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            # Maintain the increasing order in min_deque
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            # If the difference between the max and min in the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Adjust the left pointer of the window
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length

    longestSubarray = longest_subarray
