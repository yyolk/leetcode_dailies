# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/


class Solution:
    """1967. Number of Strings That Appear as Substrings in Word

    Given an array of strings patterns and a string word, return the number of
    strings in patterns that exist as a substring in word. A substring is a
    contiguous sequence of characters within a string.

    Constraints:
    * 1 <= patterns.length <= 100
    * 1 <= patterns[i].length <= 100
    * 1 <= word.length <= 100
    * patterns[i] and word consist of lowercase English letters."""

    def num_of_strings(self, patterns: list[str], word: str) -> int:
        # Initialize counter for patterns that match as substring
        count = 0
        # Iterate each pattern (O(N) with N<=100)
        for pattern in patterns:
            # Python 'in' checks substring efficiently (built-in optimized search)
            if pattern in word:
                # Increment only on exact contiguous match
                count += 1
        # Return total matching patterns
        return count

    numOfStrings = num_of_strings
