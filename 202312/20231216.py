# https://leetcode.com/problems/valid-anagram/
from collections import Counter


class Solution:
    """242. Valid Anagram

    Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and*
    `false` *otherwise*.

    An **Anagram** is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        """Determine if the input strings are anagrams of each other.

        Args:
            s: First input string.
            t: Second input string.
        
        Returns:
            True if the input strings are anagrams of each other, False if not.
        """
        # Use Counter to count occurrences of each character in both strings
        counter_s = Counter(s)
        counter_t = Counter(t)

        # Compare the Counters
        return counter_s == counter_t

    isAnagram = is_anagram
