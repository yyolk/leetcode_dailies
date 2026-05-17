# https://leetcode.com/problems/stone-game-ii/


class Solution:
    """1140. Stone Game II

    Alice and Bob continue their games with piles of stones.  There are a number of
    piles **arranged in a row**, and each pile has a positive integer number of stones
    `piles[i]`.  The objective of the game is to end with the most stones.

    Alice and Bob take turns, with Alice starting first.  Initially, `M = 1`.

    On each player's turn, that player can take **all the stones** in the **first** `X`
    remaining piles, where `1 <= X <= 2M`.  Then, we set `M = max(M, X)`.

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can
    get.

    """

    def stone_game_i_i(self, piles: list[int]) -> int:
        n = len(piles)
        # dp[i][M] will store the maximum number of stones Alice can get starting from index i with M as the current value
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # suffix_sum[i] will store the total number of stones from index i to the end
        suffix_sum = [0] * (n + 1)

        # Fill suffix_sum from the end to the beginning
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Fill the dp table
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                # Try taking X piles where 1 <= X <= 2 * M
                for X in range(1, min(2 * M, n - i) + 1):
                    # We want to maximize Alice's stones, so we subtract the optimal choice for Bob
                    dp[i][M] = max(dp[i][M], suffix_sum[i] - dp[i + X][max(M, X)])

        # The result is the maximum stones Alice can get starting from index 0 with M = 1
        return dp[0][1]

    stoneGameII = stone_game_i_i
