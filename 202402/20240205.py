# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


class Solution:
    """387. First Unique Character in a String

    Given a string `s`, *find the first non-repeating character in it and return its
    index*. If it does not exist, return `-1`.

    """

    def first_uniq_char(self, s: str) -> int:
        char_count = Counter(s)

        # Iterate through the string to find the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no non-repeating character is found, return -1
        return -1

    firstUniqChar = first_uniq_char
