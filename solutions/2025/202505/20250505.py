# https://leetcode.com/problems/domino-and-tromino-tiling/
MOD = 1_000_000_007


class Solution:
    """790. Domino and Tromino Tiling

    You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may
    rotate these shapes.

    ![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

    Given an integer n, return *the number of ways to tile an* `2 x n` *board*. Since
    the answer may be very large, return it **modulo** `10^9 + 7`.

    In a tiling, every square must be covered by a tile. Two tilings are different if
    and only if there are two 4-directionally adjacent cells on the board such that
    exactly one of the tilings has both squares occupied by a tile."""

    def num_tilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # Initialize for dp[0], dp[1], dp[2]
        dp_prev3 = 1  # dp[0]
        dp_prev2 = 1  # dp[1]
        dp_prev1 = 2  # dp[2]
        # Compute dp[i] from i=3 to n
        for i in range(3, n + 1):
            dp_current = (2 * dp_prev1 + dp_prev3) % MOD
            # Shift variables
            dp_prev3 = dp_prev2
            dp_prev2 = dp_prev1
            dp_prev1 = dp_current
        return dp_prev1

    numTilings = num_tilings
