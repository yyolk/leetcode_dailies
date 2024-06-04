# https://leetcode.com/problems/longest-palindrome/
from collections import Counter


class Solution:
    """409. Longest Palindrome

    Given a string `s` which consists of lowercase or uppercase letters, return the
    length of the **longest palindrome** that can be built with those letters.

    Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

    """

    def longest_palindrome(self, s: str) -> int:
        # Count the occurrences of each character
        count = Counter(s)
        
        # Variables to keep track of the length of the longest palindrome
        length = 0
        odd_found = False
        
        for freq in count.values():
            if freq % 2 == 0:
                # If frequency is even, add it to the length
                length += freq
            else:
                # If frequency is odd, add the largest even number less than freq
                length += freq - 1
                odd_found = True
        
        # If any odd frequency is found, add one to the length for the center character
        if odd_found:
            length += 1
        
        return length

    longestPalindrome = longest_palindrome
