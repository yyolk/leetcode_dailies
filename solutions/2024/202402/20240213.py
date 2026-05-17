# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/


class Solution:
    """2108. Find First Palindromic String in the Array

    Given an array of strings `words`, return *the first **palindromic** string in the
    array*. If there is no such string, return *an **empty string*** `""`.

    A string is **palindromic** if it reads the same forward and backward.

    """

    def first_palindrome(self, words: list[str]) -> str:
        for word in words:
            # Check if the word is a palindrome, the same forward as backwards.
            if word == word[::-1]:
                return word
        # No Palindrome is found, return an empty string.
        return ""

    firstPalindrome = first_palindrome
