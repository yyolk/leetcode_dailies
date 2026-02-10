# https://leetcode.com/problems/longest-balanced-subarray-i

class Solution:
    """3719. Longest Balanced Subarray I
    
    You are given an integer array nums.
    
    A subarray is called balanced if the number of distinct even numbers in the
    subarray is equal to the number of distinct odd numbers.
    
    Return the length of the longest balanced subarray.
    """
    def longest_balanced(self, nums: list[int]) -> int:
        # Length of the input array
        n = len(nums)
        
        # Track the maximum length of balanced subarray found
        ans = 0
        
        # Try every possible starting index i
        for i in range(n):
            # Sets for distinct even and odd values in current subarray
            evens = set()
            odds = set()
            
            # Extend the subarray to every possible ending index j >= i
            for j in range(i, n):
                num = nums[j]
                
                # Add number to the corresponding set (duplicates ignored)
                if num % 2 == 0:
                    evens.add(num)
                else:
                    odds.add(num)
                
                # If distinct counts match, update the answer
                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)
        
        return ans

    longestBalanced = longest_balanced