# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    """1143. Longest Common Subsequence

    Given two strings `text1` and `text2`, return *the length of their longest **common
    subsequence**.* If there is no **common subsequence**, return `0`.

    A **subsequence** of a string is a new string generated from the original string
    with some characters (can be none) deleted without changing the relative order of
    the remaining characters.

    * For example, `"ace"` is a subsequence of `"abcde"`.

    A **common subsequence** of two strings is a subsequence that is common to both
    strings.
    """

    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Initialize a 2D array to store the lengths of common subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the DP array
        return dp[m][n]

    longestCommonSubsequence = longest_common_subsequence
