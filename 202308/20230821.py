# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    """459. Repeated Substring Pattern

    Given a string s, check if it can be constructed by taking a substring of it and
    appending multiple copies of the substring together.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        """Determines if s is a repeating substring

        Proposed solution using an algorithm to extract substrings and add them
        together to see if they match the input.

        Args:
            s (str): input string to check for substring pattern

        Returns:
            bool: True if repeating substring creates input
        """
        length_s = len(s)
        for i in range(1, length_s // 2 + 1):
            if length_s % i == 0:
                substring = s[:i]
                # Try repeating the substring for the total length_s // i
                repeated_string = substring * (length_s // i)
                if repeated_string == s:
                    # We found a repeating substring
                    return True
        # No repeating substring found
        return False
