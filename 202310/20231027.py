# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    """5. Longest Palindromic Substring

    Given a string `s`, return *the longest* *palindromic* *substring* in `s`.
    """

    def longest_palindrome(self, s: str) -> str:
        """The longest palindromic substring from input s.

        Proposed solution using dynamic programming.

        Args:
            s (str): The input string to search.
        Returns:
            str: The palindromic substring that's the longest from s.
        """

        def expand_around_center(left, right):
            """Helper function to expand around a center and find a palindrome."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When the loop ends, s[left + 1 : right] is the palindrome found
            return s[left + 1 : right]

        # Initialize a variable to store the longest palindrome
        longest = ""

        # Iterate through the characters in the string
        for i in range(len(s)):
            # Find the longest odd length palindrome with the current character as the
            # center
            palindrome_odd = expand_around_center(i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd

            # Find the longest even length palindrome with the current character as the
            # center
            palindrome_even = expand_around_center(i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even

        # Return the longest palindrome found
        return longest

    longestPalindrome = longest_palindrome
