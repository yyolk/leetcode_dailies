# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
from string import ascii_lowercase


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

    * For example, `"ace"` is a subsequence of `"abcde"`.
    """

    def count_palindromic_subsequence(self, s: str) -> int:
        """
        Counts unique subsequences of input that are length of 3.

        Args:
            s: Input string to find subsequences from.

        Returns:
            The number of unique, palindromic subsequences that are length of 3.
        """
        count = 0

        # Find the first and last occurrence of c, every unique character in between
        # would make a unique palindromic occurrence of length 3.
        for c in ascii_lowercase:
            first, last = s.find(c), s.rfind(c)
            if first > -1:
                count += len(set(s[first + 1 : last]))

        return count

    countPalindromicSubsequence = count_palindromic_subsequence
