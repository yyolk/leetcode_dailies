# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
from collections import Counter


class Solution:
    """2131. Longest Palindrome by Concatenating Two Letter Words

    You are given an array of strings `words`. Each element of `words` consists of
    **two** lowercase English letters.

    Create the **longest possible palindrome** by selecting some elements from `words`
    and concatenating them in **any order**. Each element can be selected **at most
    once**.

    Return *the **length** of the longest palindrome that you can create*. If it is
    impossible to create any palindrome, return `0`.

    A **palindrome** is a string that reads the same forward and backward."""

    def longest_palindrome(self, words: list[str]) -> int:
        # Count the frequency of each word
        freq = Counter(words)
        total_length = 0
        has_center = False

        # Process each unique word
        for word in list(freq.keys()):
            # Get the reverse of the word
            rev = word[::-1]
            if rev in freq and freq[rev] > 0:
                if word == rev:  # Word is a palindrome (e.g., "aa")
                    pairs = freq[word] // 2
                    total_length += pairs * 4  # Each pair contributes 4 letters
                    freq[word] -= pairs * 2  # Use up the paired words
                    if freq[word] > 0:  # If any remain, can use one in center
                        has_center = True
                else:  # Word and its reverse are different (e.g., "ab" and "ba")
                    pairs = min(freq[word], freq[rev])
                    total_length += pairs * 4  # Each pair contributes 4 letters
                    freq[word] -= pairs  # Use up the paired words
                    freq[rev] -= pairs

        # Add 2 to the length if we can place a palindrome word in the center
        if has_center:
            total_length += 2

        return total_length

    longestPalindrome = longest_palindrome
