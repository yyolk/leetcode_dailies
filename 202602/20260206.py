# https://leetcode.com/problems/minimum-removals-to-balance-array

class Solution:
    """3634. Minimum Removals to Balance Array
    
    You are given an integer array nums and an integer k.
    
    An array is considered balanced if the value of its maximum element is
    at most k times the minimum element.
    
    You may remove any number of elements from nums without making it empty.
    
    Return the minimum number of elements to remove so that the remaining
    array is balanced.
    
    Note: An array of size 1 is considered balanced as its maximum and
    minimum are equal, and the condition always holds true.
    """
    def min_removal(self, nums: list[int], k: int) -> int:
        # Sort in non-decreasing order to check windows where min is left,
        # max is right
        nums.sort()
        
        n = len(nums)
        
        # Left pointer for the start of the current window
        left = 0
        
        # Track the maximum number of elements we can keep
        max_keep = 0
        
        # Expand the window with right pointer
        for right in range(n):
            # Shrink from left while max > k * min in current window
            while left <= right and nums[right] > k * nums[left]:
                left += 1
            
            # Current window [left..right] satisfies nums[right] <= k * nums[left]
            max_keep = max(max_keep, right - left + 1)
        
        # Minimum removals = total elements - maximum keepable
        return n - max_keep

    minRemoval = min_removal