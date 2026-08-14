# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/


class Solution:
    """3090. Maximum Length Substring With Two Occurrences

    Given a string `s`, return the **maximum** length of a substring such that it
    contains *at most two occurrences* of each character.

    Constraints:

    * `2 <= s.length <= 100`

    * `s` consists only of lowercase English letters."""

    def maximum_length_substring(self, s: str) -> int:
        """Return the longest substring where each char appears at most twice."""
        left = 0
        counts: dict[str, int] = {}
        best = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            while counts[char] > 2:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best

    maximumLengthSubstring = maximum_length_substring
