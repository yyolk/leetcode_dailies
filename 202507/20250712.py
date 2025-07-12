# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/


class Solution:
    """1900. The Earliest and Latest Rounds Where Players Compete

    There is a tournament where `n` players are participating. The players are standing
    in a single row and are numbered from `1` to `n` based on their **initial** standing
    position (player `1` is the first player in the row, player `2` is the second player
    in the row, etc.).

    The tournament consists of multiple rounds (starting from round number `1`). In each
    round, the `ith` player from the front of the row competes against the `ith` player
    from the end of the row, and the winner advances to the next round. When the number
    of players is odd for the current round, the player in the middle automatically
    advances to the next round.

    * For example, if the row consists of players `1, 2, 4, 6, 7`

      + Player `1` competes against player `7`.

      + Player `2` competes against player `6`.

      + Player `4` automatically advances to the next round.

    After each round is over, the winners are lined back up in the row based on the
    **original ordering** assigned to them initially (ascending order).

    The players numbered `first_player` and `second_player` are the best in the
    tournament. They can win against any other player before they compete against each
    other. If any two other players compete against each other, either of them might
    win, and thus you may **choose** the outcome of this round.

    Given the integers `n`, `first_player`, and `second_player`, return *an integer
    array containing two values, the **earliest** possible round number and the
    **latest** possible round number in which these two players will compete against
    each other, respectively*."""

    def earliest_and_latest(
        self, n: int, first_player: int, second_player: int
    ) -> list[int]: ...

    earliestAndLatest = earliest_and_latest
