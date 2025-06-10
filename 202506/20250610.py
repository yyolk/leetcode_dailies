# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
from collections import Counter


class Solution:
    """3442. Maximum Difference Between Even and Odd Frequency I

    You are given a string `s` consisting of lowercase English letters.

    Your task is to find the **maximum** difference `diff = a1 - a2` between the
    frequency of characters `a1` and `a2` in the string such that:

    * `a1` has an **odd frequency** in the string.

    * `a2` has an **even frequency** in the string.

    Return this **maximum** difference."""

    def max_difference(self, s: str) -> int:
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # Initialize max_odd to -1 (no odd frequency found yet)
        # Initialize min_even to len(s) + 1 (larger than any possible frequency)
        max_odd = -1
        min_even = len(s) + 1
        
        # Iterate through the frequency of each character
        for count in freq.values():
            if count % 2 == 1:  # Odd frequency
                max_odd = max(max_odd, count)
            elif count % 2 == 0:  # Even frequency
                min_even = min(min_even, count)
        
        # Check if we found both an odd and an even frequency
        if max_odd != -1 and min_even <= len(s):
            return max_odd - min_even
        else:
            return 0

    maxDifference = max_difference
