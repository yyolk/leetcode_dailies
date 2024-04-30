# https://leetcode.com/problems/number-of-wonderful-substrings/


class Solution:
    """1915. Number of Wonderful Substrings

    A **wonderful** string is a string where **at most one** letter appears an **odd**
    number of times.

    * For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

    Given a string `word` that consists of the first ten lowercase English letters
    (`'a'` through `'j'`), return *the **number of wonderful non-empty substrings** in*
    `word`*. If the same substring appears multiple times in* `word`*, then count **each
    occurrence** separately.*

    A **substring** is a contiguous sequence of characters in a string.

    """

    def wonderful_substrings(self, word: str) -> int:
        # Initialize count of wonderful substrings and prefix count array
        count = 0
        # 2^10 for 10 lowercase letters
        prefix_count = [0] * 1024
        # Initialize the count for an empty string (all even parity)
        prefix_count[0] = 1
        # Initialize the bitmask to track parity
        mask = 0

        # Iterate through each character in the word
        for char in word:
            # Update the bitmask with the parity information of the current character
            mask ^= 1 << (ord(char) - ord('a'))
            # Increment the count by the number of substrings with the same parity as the current mask
            count += prefix_count[mask]

            # Increment the count by the number of substrings with one character difference in parity
            for i in range(10):
                count += prefix_count[mask ^ (1 << i)]

            # Update the prefix count for the current mask
            prefix_count[mask] += 1

        # Return the total count of wonderful substrings
        return count

    wonderfulSubstrings = wonderful_substrings
