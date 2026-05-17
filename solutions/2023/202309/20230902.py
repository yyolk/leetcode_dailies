# https://leetcode.com/problems/extra-characters-in-a-string/


class Solution:
    """2707. Extra Characters in a String

    You are given a **0-indexed** string `s` and a dictionary of words `dictionary`.
    You have to break `s` into one or more **non-overlapping** substrings such that
    each substring is present in `dictionary`. There may be some **extra characters**
    in `s` which are not present in any of the substrings.

    Return *the **minimum** number of extra characters left over if you break up* `s`
    *optimally.*
    """

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """Extract the minimum number of extra characters

        Proposed solution

        Args:
            s (str): The input string which must be broken up
            dictionary (list of str): A literal dictionary of substrings to match input
                `s` to

        Returns:
            int: The minimum number of extra characters left over if you break up `s` optimally
        """
        # We'll frequently re-use this length, set to n
        n = len(s)
        # A holding list for all the letters we'll use
        # Assume all characters are extra initially
        dp = [n] * (n + 1)
        # Empty string case
        dp[0] = 0

        # Loop through the positions in the string s
        for i in range(1, n + 1):
            # Check each word in the dictionary to see if it matches the substring ending at position i
            for word in dictionary:
                if i >= len(word) and s[i - len(word) : i] == word:
                    # If the word matches, update dp[i] with the minimum extra characters needed
                    dp[i] = min(dp[i], dp[i - len(word)])

            # Update dp[i] to consider not breaking the string at this position
            dp[i] = min(dp[i], dp[i - 1] + 1)

        # Return the value at the end of the dp array, which now represents the minimum extra characters
        return dp[n]
