# https://leetcode.com/problems/stone-removal-game/


class Solution:
    """3360. Stone Removal Game

    Alice and Bob are playing a game where they take turns removing stones
    from a pile, with *Alice going first*.

    * Alice starts by removing **exactly** 10 stones on her first turn.

    * For each subsequent turn, each player removes **exactly** 1 fewer
    stone than the previous opponent.

    The player who cannot make a move loses the game.

    Given a positive integer `n`, return `true` if Alice wins the game and
    `false` otherwise.

    Constraints:

    * `1 <= n <= 50`
    """

    def can_alice_win(self, n: int) -> bool:
        # Simulate the decreasing removal amounts starting from 10.
        remove = 10
        is_alice_turn = True
        while remove > 0:
            # Current player cannot take the required number of stones.
            if n < remove:
                return not is_alice_turn
            n -= remove
            remove -= 1
            is_alice_turn = not is_alice_turn
        # Full sequence of positive removals exhausted.
        return not is_alice_turn

    canAliceWin = can_alice_win
