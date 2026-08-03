# https://leetcode.com/problems/stone-game-iii/


class Solution:
    """1406. Stone Game III

    Alice and Bob continue their games with piles of stones. There are several stones
    **arranged in a row**, and each stone has an associated value which is an integer
    given in the array `stone_value`.

    Alice and Bob take turns, with Alice starting first. On each player's turn, that
    player can take `1`, `2`, or `3` stones from the **first** remaining stones in the
    row.

    The score of each player is the sum of the values of the stones taken. The score of
    each player is `0` initially.

    The objective of the game is to end with the highest score, and the winner is the
    player with the highest score and there could be a tie. The game continues until all
    the stones have been taken.

    Assume Alice and Bob **play optimally**.

    Return `"Alice"` *if Alice will win,* `"Bob"` *if Bob will win, or* `"Tie"` *if they
    will end the game with the same score*.

    Constraints:

    * `1 <= stone_value.length <= 5 * 104`

    * `-1000 <= stone_value[i] <= 1000`"""

    def stone_game_i_i_i(self, stone_value: list[int]) -> str:
        """...

        Proposed solution ...

        Args:
            stone_value (list of int): ...

        Returns:
            str: ..."""
        n = len(stone_value)
        # dp[i] = best score difference current player can achieve from index i.
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            take = 0
            best = -10**9
            for j in range(i, min(i + 3, n)):
                take += stone_value[j]
                best = max(best, take - dp[j + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"

    stoneGameIII = stone_game_i_i_i
