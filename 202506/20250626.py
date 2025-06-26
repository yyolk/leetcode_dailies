# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/


class Solution:
    """2311. Longest Binary Subsequence Less Than or Equal to K

    You are given a binary string `s` and a positive integer `k`.

    Return *the length of the **longest** subsequence of* `s` *that makes up a
    **binary** number less than or equal to* `k`.

    Note:

    * The subsequence can contain **leading zeroes**.

    * The empty string is considered to be equal to `0`.

    * A **subsequence** is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters."""

    def longest_subsequence(self, s: str, k: int) -> int:
        n = len(s)
        # A large number to represent infinity
        INF = 10**18
        # dp[l] is the smallest value for subsequence of length l
        dp = [INF] * (n + 1)
        # Empty subsequence has value 0
        dp[0] = 0

        # Process each character in the string
        for i in range(n):
            # Update dp array from right to left
            for l in range(n, -1, -1):
                if dp[l] <= k:
                    # Calculate new value if current character is included
                    new_value = 2 * dp[l] + int(s[i])
                    if new_value < dp[l + 1]:
                        dp[l + 1] = new_value

        # Find the largest length l where dp[l] <= k
        for l in range(n, -1, -1):
            if dp[l] <= k:
                return l
        # Fallback, though dp[0] should always be 0 <= k
        return 0

    longestSubsequence = longest_subsequence
