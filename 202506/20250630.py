# https://leetcode.com/problems/longest-harmonious-subsequence/
from collections import Counter


class Solution:
    """594. Longest Harmonious Subsequence

    We define a harmonious array as an array where the difference between its maximum
    value and its minimum value is **exactly** `1`.

    Given an integer array `nums`, return the length of its longest harmonious
    subsequence among all its possible subsequences."""

    def find_l_h_s(self, nums: list[int]) -> int:
        # Count the frequency of each number in the array
        counter = Counter(nums)
        max_length = 0
        
        # Check each unique number and its consecutive number
        for x in counter:
            if x + 1 in counter:
                # Calculate length of subsequence with x and x+1
                current_length = counter[x] + counter[x + 1]
                # Update max_length if current_length is greater
                max_length = max(max_length, current_length)
                
        return max_length

    findLHS = find_l_h_s
