# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/
# Define the modulo constant
MOD = 10**9 + 7


class Solution:
    """2787. Ways to Express an Integer as Sum of Powers

    Given two **positive** integers `n` and `x`.

    Return *the number of ways* `n` *can be expressed as the sum of the* `xth` *power of
    **unique** positive integers, in other words, the number of sets of unique integers*
    `[n1, n2, ..., nk]` *where* `n = n1x + n2x + ... + nkx`*.*

    Since the result can be very large, return it modulo `109 + 7`.

    For example, if `n = 160` and `x = 3`, one way to express `n` is `n = 23 + 33 + 53`.
    """

    def number_of_ways(self, n: int, x: int) -> int:
        # Generate the list of possible x-th powers <= n
        powers = []
        k = 1
        while True:
            p = k**x
            if p > n:
                break
            powers.append(p)
            k += 1

        # Initialize dp array where dp[j] is the number of ways to sum to j
        dp = [0] * (n + 1)
        dp[0] = 1

        # Update dp for each power using 0-1 knapsack style
        for p in powers:
            for j in range(n, p - 1, -1):
                dp[j] = (dp[j] + dp[j - p]) % MOD

        # Return the number of ways for n
        return dp[n]

    numberOfWays = number_of_ways
