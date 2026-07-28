# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/


class Solution:
    """3517. Smallest Palindromic Rearrangement I

    You are given a **palindromic** string `s`.
    Return the **lexicographically smallest** palindromic
    permutation of `s`.

    Constraints:
    * `1 <= s.length <= 10^5`
    * `s` consists of lowercase English letters.
    * `s` is guaranteed to be palindromic.
    """

    def smallest_palindrome(self, s: str) -> str:
        # Count frequency of each lowercase letter
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        # Build left half using half counts, a-z order for lex smallest
        left_parts = []
        middle = ""
        for i in range(26):
            count = freq[i]
            char = chr(ord("a") + i)
            # Take half the occurrences for the first half
            left_parts.append(char * (count // 2))
            # Capture the single middle character if count is odd
            if count % 2:
                middle = char

        left = "".join(left_parts)
        # Form the palindrome: left + middle + reverse(left)
        return left + middle + left[::-1]

    smallestPalindrome = smallest_palindrome
