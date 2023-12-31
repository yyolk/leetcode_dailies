# https://leetcode.com/problems/largest-substring-between-two-equal-characters/


class Solution:
    """1624. Largest Substring Between Two Equal Characters

    Given a string `s`, return *the length of the longest substring between two equal
    characters, excluding the two characters.* If there is no such substring return
    `-1`.

    A **substring** is a contiguous sequence of characters within a string.
    """

    def max_length_between_equal_characters(self, s: str) -> int:
        max_length = -1

        # Iterate over all unique instances of characters.
        for char in set(s):
            # Pull the left-most position of char from s.
            start = s.find(char)
            # Pull the right-most position of char from s.
            end = s.rfind(char)

            # If they're not in the same position, update the max_length.
            if start != end:
                max_length = max(max_length, end - start - 1)

        # Return the computed max_length
        return max_length

    maxLengthBetweenEqualCharacters = max_length_between_equal_characters
