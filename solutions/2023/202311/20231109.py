# https://leetcode.com/problems/count-number-of-homogenous-substrings/


class Solution:
    """1759. Count Number of Homogenous Substrings

    Given a string `s`, return *the number of **homogenous** substrings of* `s`*.* Since
    the answer may be too large, return it **modulo** `10^9 + 7`.

    A string is **homogenous** if all the characters of the string are the same.

    A **substring** is a contiguous sequence of characters within a string.
    """

    def count_homogenous(self, s: str) -> int:
        """Count the number of homogenous substrings in the given string.

        Args:
            s: The input string.

        Returns:
            The number of homogenous substrings modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        result = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result = (result + count * (count + 1) // 2) % MOD
                count = 1

        # Add the count for the last homogenous substring
        result = (result + count * (count + 1) // 2) % MOD

        return result

    countHomogenous = count_homogenous
