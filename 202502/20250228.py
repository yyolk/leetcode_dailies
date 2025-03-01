# https://leetcode.com/problems/shortest-common-supersequence/


class Solution:
    """1092. Shortest Common Supersequence

    Given two strings `str1` and `str2`, return *the shortest string that has both*
    `str1` *and* `str2` *as **subsequences***. If there are multiple valid strings,
    return **any** of them.

    A string `s` is a **subsequence** of string `t` if deleting some number of
    characters from `t` (possibly `0`) results in the string `s`."""

    def shortest_common_supersequence(self, str1: str, str2: str) -> str:
        # Get lengths of input strings
        m, n = len(str1), len(str2)

        # Initialize DP table for LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill DP table to compute LCS length
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Build SCS by tracing back through DP table
        res = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # Characters match (part of LCS), include once and move diagonally
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # LCS comes from str1 excluding current char, include str1[i-1]
                res.append(str1[i - 1])
                i -= 1
            else:
                # LCS comes from str2 excluding current char, or equal, include str2[j-1]
                res.append(str2[j - 1])
                j -= 1

        # Append remaining characters from str1, if any
        while i > 0:
            res.append(str1[i - 1])
            i -= 1

        # Append remaining characters from str2, if any
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        # Reverse the result since we built it backwards, then join into a string
        return "".join(reversed(res))

    shortestCommonSupersequence = shortest_common_supersequence
