# https://leetcode.com/problems/stone-game-iv/


class Solution:
    """1510. Stone Game IV

    Alice and Bob take turns playing a game, with Alice starting first.

    Initially, there are `n` stones in a pile. On each player's turn, that player makes
    a *move* consisting of removing **any** non-zero **square number** of stones in the
    pile.

    Also, if a player cannot make a move, he/she loses the game.

    Given a positive integer `n`, return `true` if and only if Alice wins the game
    otherwise return `false`, assuming both players play optimally.

    Constraints:

    * `1 <= n <= 105`"""

    def winner_square_game(self, n: int) -> bool:
        """Return whether Alice can force a win with optimal play."""
        can_win = [False] * (n + 1)
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for stones in range(1, n + 1):
            for square in squares:
                if square > stones:
                    break
                if not can_win[stones - square]:
                    can_win[stones] = True
                    break

        return can_win[n]

    winnerSquareGame = winner_square_game
