# https://leetcode.com/problems/stone-game-ix/


class Solution:
    """2029. Stone Game IX

    Alice and Bob continue their games with stones. There is a row of n stones, and each
    stone has an associated value. You are given an integer array `stones`, where
    `stones[i]` is the **value** of the `ith` stone.

    Alice and Bob take turns, with **Alice** starting first. On each turn, the player
    may remove any stone from `stones`. The player who removes a stone **loses** if the
    **sum** of the values of **all removed stones** is divisible by `3`. Bob will win
    automatically if there are no remaining stones (even if it is Alice's turn).

    Assuming both players play **optimally**, return `true` *if Alice wins and* `false`
    *if Bob wins*.

    Constraints:

    * `1 <= stones.length <= 105`

    * `1 <= stones[i] <= 104`"""

    def stone_game_i_x(self, stones: list[int]) -> bool:
        """Return True when Alice can force a win."""
        counts = [0, 0, 0]
        for stone in stones:
            counts[stone % 3] += 1

        zeros, ones, twos = counts

        if zeros % 2 == 0:
            return ones > 0 and twos > 0

        return abs(ones - twos) > 2

    stoneGameIX = stone_game_i_x
