# https://leetcode.com/problems/trionic-array-i/description/

class Solution:
    """3637. Trionic Array I
    
    You are given an integer array nums of length n.
    An array is trionic if there exist indices 0 < p < q < n-1 such that:
    nums[0...p] is strictly increasing,
    nums[p...q] is strictly decreasing,
    nums[q...n-1] is strictly increasing.
    Return true if nums is trionic, otherwise return false.
    """
    def is_trionic(self, nums: list[int]) -> bool:
        n = len(nums)
        # Minimum length required for valid p and q
        if n < 4:
            return False
        
        # Find end of longest strict increasing prefix (potential peak p)
        p = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                p = i
            else:
                break
        
        # Need at least one strict increase (p >= 1)
        if p < 1:
            return False
        
        # Must strictly decrease immediately after peak
        if p + 1 >= n or nums[p + 1] >= nums[p]:
            return False
        
        # Find end of longest strict decreasing segment from p (potential valley q)
        q = p
        i = p + 1
        while i < n and nums[i] < nums[i - 1]:
            q = i
            i += 1
        
        # Need at least two elements for final increasing part
        if q + 1 >= n:
            return False
        
        # Must strictly increase immediately after valley
        if nums[q + 1] <= nums[q]:
            return False
        
        # Verify entire suffix from q+1 to end is strictly increasing
        for j in range(q + 2, n):
            if nums[j] <= nums[j - 1]:
                return False
        
        return True

    isTrionic = is_trionic