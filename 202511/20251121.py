# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
from string import ascii_lowercase


class Solution:
    """1930. Unique Length-3 Palindromic Subsequences

    Given a string `s`, return the number of unique palindromes of length three
    that are a subsequence of `s`.

    Note that even if there are multiple ways to obtain the same subsequence,
    it is still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original
    string with some characters (can be none) deleted without changing the
    relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    """
    def count_palindromic_subsequence(self, s: str) -> int:
        count = 0
        # Iterate over each possible outer character (a-z)
        for c in ascii_lowercase:
            # Find leftmost and rightmost occurrence of c
            first = s.find(c)
            last = s.rfind(c)
            # Need at least two occurrences to form aba pattern
            if first >= 0 and first < last:
                # Count unique characters strictly between first and last c
                # Using set on slice is concise and fast enough (n<=1000)
                count += len(set(s[first + 1:last]))
        return count

    countPalindromicSubsequence = count_palindromic_subsequence