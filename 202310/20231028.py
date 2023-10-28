# https://leetcode.com/problems/count-vowels-permutation/
MOD = 10**9 + 7


class Solution:
    """1220. Count Vowels Permutation

    Given an integer `n`, your task is to count how many strings of length `n` can be
    formed under the following rules:

    * Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)

    * Each vowel `'a'` may only be followed by an `'e'`.

    * Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.

    * Each vowel `'i'` **may not** be followed by another `'i'`.

    * Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.

    * Each vowel `'u'` may only be followed by an `'a'.`

    Since the answer may be too large, return it modulo `10^9 + 7.`
    """

    def count_vowel_permutation(self, n: int) -> int:
        """How many strings of length n can be formed under the rules.

        Proposed solution using dynamic programming.

        Args:
            n (int): The input target length to form strings.

        Returns:
            int: The maximum amount of strings that can be formed for target length n
                cutoff at 10^9 + 7.
        """
        # Initialize the dp array with 0s.
        dp = [[0] * 5 for _ in range(n + 1)]

        # Base case: there's 1 valid string of length 1 for each vowel.
        for j in range(5):
            dp[1][j] = 1

        for i in range(2, n + 1):
            # Calculate the number of valid strings of length i for each vowel.
            # 'a' can only be followed by 'e'
            dp[i][0] = dp[i - 1][1]
            # 'e' can only be followed by 'a' or 'i'
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            # 'i' cannot be followed by another 'i'
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
            # 'o' can be followed by 'i' or 'u'
            dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % MOD
            # 'u' can only be followed by 'a'
            dp[i][4] = dp[i - 1][0]

        # Calculate the total count of valid strings of length n, cut to MOD, and return it
        return sum(dp[n]) % MOD

    countVowelPermutation = count_vowel_permutation
