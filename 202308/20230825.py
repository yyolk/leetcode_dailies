class Solution:
    """97. Interleaving

    Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving
    of `s1` and `s2`.

    An **interleaving** of two strings `s` and `t` is a configuration where `s` and
    `t` are divided into `n` and `m` substrings respectively, such that:

    * `s = s1 + s2 + ... + sn`
    * `t = t1 + t2 + ... + tm`
    * `|n - m| <= 1`
    * The **interleaving** is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or
    `t1 + s1 + t2 + s2 + t3 + s3 + ...`

    **Note**: `a + b` is the concatenation of strings `a` and `b`.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Determines if s3 is formed by an interleaving of s1 and s2

        Proposed solution using dynamic programming and a 1D array.

        Args:
            s1 (str): first input string
            s2 (str): second input string
            s3 (str): third input, which we'll determine if was formed by an
                interleaving of the previous 2 inputs

        Returns:
            bool: if s3 is an interleaving of s1 and s2
        """
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        # Check if the total length of s1 and s2 equals s3.
        if len_s1 + len_s2 != len_s3:
            return False

        # Swap s1 and s2 if s2 is shorter to minimize space usage.
        if len_s1 < len_s2:
            s1, s2, len_s1, len_s2 = s2, s1, len_s2, len_s1

        # Initialize a 1D DP array with length len_s2 (or len_s1 if len_s2 is smaller).
        dp = [False] * (len_s2 + 1)
        # An empty s1 and s2 can form an empty s3.
        dp[0] = True

        # Update DP array based on both s1 and s2.
        for j in range(1, len_s2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Update DP array based on both s1 and s2.
        for i in range(1, len_s1 + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len_s2 + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        # The final value in dp[len_s2] represents whether s3 can be formed by
        # interleaving s1 and s2.
        return dp[len_s2]
