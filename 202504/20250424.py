# https://leetcode.com/problems/count-complete-subarrays-in-an-array/


class Solution:
    """2799. Count Complete Subarrays in an Array

    You are given an array `nums` consisting of **positive** integers.

    We call a subarray of an array **complete** if the following condition is satisfied:

    * The number of **distinct** elements in the subarray is equal to the number of
    distinct elements in the whole array.

    Return *the number of **complete** subarrays*.

    A **subarray** is a contiguous non-empty part of an array."""

    def count_complete_subarrays(self, nums: list[int]) -> int:
        # Length of the array
        n = len(nums)
        # Number of distinct elements in the entire array
        k = len(set(nums))
        # Target for at_most calculation
        m = k - 1
        # Total number of possible subarrays
        total = n * (n + 1) // 2
        
        # Helper function to count subarrays with at most m distinct elements
        def at_most(m):
            count = 0
            left = 0
            counter = defaultdict(int)
            distinct = 0
            
            # Iterate over all possible right endpoints
            for right in range(n):
                # Add the right element to the window
                if counter[nums[right]] == 0:
                    distinct += 1
                counter[nums[right]] += 1
                
                # Shrink the window if distinct elements exceed m
                while distinct > m and left <= right:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                
                # Add the number of valid subarrays ending at right
                count += right - left + 1
            
            return count
        
        # Number of complete subarrays = total - subarrays with at most k-1 distinct elements
        return total - at_most(m)

    countCompleteSubarrays = count_complete_subarrays
