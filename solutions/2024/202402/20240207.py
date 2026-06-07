# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter


class Solution:
    """451. Sort Characters By Frequency

    Given a string `s`, sort it in **decreasing order** based on the **frequency** of
    the characters. The **frequency** of a character is the number of times it appears
    in the string.

    Return *the sorted string*. If there are multiple answers, return *any of them*.

    """

    def frequency_sort(self, s: str) -> str:
        # Count the frequency of each character in the string
        char_freq = Counter(s)

        # Sort the characters based on their frequency in decreasing order
        sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)

        # Build the sorted string by repeating each character according to its frequency
        result = "".join(char * char_freq[char] for char in sorted_chars)

        return result

    frequencySort = frequency_sort
