# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii

class Solution:
    """3130. Find All Possible Stable Binary Arrays II

    You are given 3 positive integers zero, one, and limit. A binary array arr is
    called stable if: The number of occurrences of 0 in arr is exactly zero. The
    number of occurrences of 1 in arr is exactly one. Each subarray of arr with
    size > limit must contain both 0 and 1. Return the total number of stable
    binary arrays modulo 10^9 + 7.
    """
    def number_of_stable_arrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k]: ways using i zeros, j ones, ending with k (0 or 1)
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        # Base: sequences of only zeros (up to limit)
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1

        # Base: sequences of only ones (up to limit)
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Ending with 0: all (i-1, j) append 0 minus invalid long 0-runs
                prev = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                sub = dp[i - limit - 1][j][1] if i - limit - 1 >= 0 else 0
                dp[i][j][0] = (prev - sub + MOD) % MOD

                # Ending with 1: symmetric
                prev = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                sub = dp[i][j - limit - 1][0] if j - limit - 1 >= 0 else 0
                dp[i][j][1] = (prev - sub + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD

    numberOfStableArrays = number_of_stable_arrays