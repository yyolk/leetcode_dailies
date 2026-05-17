# https://leetcode.com/problems/determine-if-two-strings-are-close/
from collections import Counter


class Solution:
    """1657. Determine if Two Strings Are Close

    Two strings are considered **close** if you can attain one from the other using the
    following operations:

    * Operation 1: Swap any two **existing** characters.

            + For example, `abcde -> aecdb`

    * Operation 2: Transform **every** occurrence of one **existing** character into
    another **existing** character, and do the same with the other character.

            + For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s
    turn into `a`'s)

    You can use the operations on either string as many times as necessary.

    Given two strings, `word1` and `word2`, return `true` *if* `word1` *and* `word2`
    *are **close**, and* `false` *otherwise.*
    """

    def close_strings(self, word1: str, word2: str) -> bool:
        # Check if the lengths of the two words are equal
        if len(word1) != len(word2):
            return False

        # Count the occurrences of each character in both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Check if the sets of characters are the same
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if the frequency counts of characters are the same
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True

    closeStrings = close_strings
