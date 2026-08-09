# https://leetcode.com/problems/stone-game-ii/


class Solution:
    """1140. Stone Game II

    Alice and Bob continue their games with piles of stones. There are a number of piles
    **arranged in a row**, and each pile has a positive integer number of stones
    `piles[i]`. The objective of the game is to end with the most stones.

    Alice and Bob take turns, with Alice starting first.

    On each player's turn, that player can take **all the stones** in the **first** `X`
    remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`. Initially, M =
    1.

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can
    get.

    Constraints:

    * `1 <= piles.length <= 100`

    * `1 <= piles[i] <= 104`"""

    def stone_game_i_i(self, piles: list[int]) -> int:
        """Return the maximum stones Alice can collect with optimal play."""
        from functools import lru_cache

        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def best(start: int, m: int) -> int:
            if start + 2 * m >= n:
                return suffix[start]

            opponent_best = suffix[start]
            limit = min(n - start, 2 * m)
            for x in range(1, limit + 1):
                opponent_best = min(opponent_best, best(start + x, max(m, x)))

            return suffix[start] - opponent_best

        return best(0, 1)

    stoneGameII = stone_game_i_i
