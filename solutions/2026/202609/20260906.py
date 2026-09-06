# https://leetcode.com/problems/distinct-subsequences/


class Solution:
    """115. Distinct Subsequences

    Given two strings s and t, return the number of distinct subsequences of s
    which equals t.

    The test cases are generated so that the answer fits on a 32-bit signed
    integer.

    Constraints:

    * 1 <= s.length, t.length <= 1000

    * s and t consist of English letters.
    """

    def num_distinct(self, s: str, t: str) -> int:
        # 1D DP: dp[j] = number of ways to form t[:j] with current prefix of s
        n = len(t)
        dp = [1] + [0] * n
        for char in s:
            # Traverse right-to-left so we use previous (unupdated) values
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]

    numDistinct = num_distinct
