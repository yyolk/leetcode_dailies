# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/


class Solution:
    """1930. Unique Length-3 Palindromic Subsequences

    Given a string `s`, return *the number of **unique palindromes of length three**
    that are a **subsequence** of* `s`.

    Note that even if there are multiple ways to obtain the same subsequence, it is
    still only counted **once**.

    A **palindrome** is a string that reads the same forwards and backwards.

    A **subsequence** of a string is a new string generated from the original string
    with some characters (can be none) deleted without changing the relative order of
    the remaining characters.

    * For example, `"ace"` is a subsequence of `"abcde"`."""

    def count_palindromic_subsequence(self, s: str) -> int: ...

    countPalindromicSubsequence = count_palindromic_subsequence
