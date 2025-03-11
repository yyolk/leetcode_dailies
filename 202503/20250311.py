# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


class Solution:
    """1358. Number of Substrings Containing All Three Characters

    Given a string `s` consisting only of characters *a*, *b* and *c*.

    Return the number of substrings containing **at least** one occurrence of all these
    characters *a*, *b* and *c*."""

    def number_of_substrings(self, s: str) -> int:
        # Initialize count of valid substrings
        count = 0

        # Dictionary to keep track of character frequencies in current window
        char_count = {"a": 0, "b": 0, "c": 0}

        # Left pointer of sliding window
        left = 0

        # Iterate through string with right pointer
        for right in range(len(s)):
            # Add current character to frequency count
            char_count[s[right]] += 1

            # While window has at least one of each character
            while (
                char_count["a"] >= 1 and char_count["b"] >= 1 and char_count["c"] >= 1
            ):
                # All substrings from left to end of string are valid
                # Add their count (len(s) - right) to total
                count += len(s) - right

                # Shrink window by removing leftmost character
                char_count[s[left]] -= 1
                left += 1

        return count

    numberOfSubstrings = number_of_substrings
