# https://leetcode.com/problems/count-of-matches-in-tournament/


class Solution:
    """1688. Count of Matches in Tournament

    You are given an integer `n`, the number of teams in a tournament that has strange
    rules:

    * If the current number of teams is **even**, each team gets paired with another
    team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next
    round.

    * If the current number of teams is **odd**, one team randomly advances in the
    tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played,
    and `(n - 1) / 2 + 1` teams advance to the next round.

    Return *the number of matches played in the tournament until a winner is decided.*
    """

    def number_of_matches(self, n: int) -> int:
        """Given n teams, find the number of matches.

        This simple calculation works because it will determine the number of matches
        played based on the number of teams, until a winner is decided based on the
        given rules.

        A winner will always be `number of teams - 1`, to have full participation and
        a winning match to decide amongst the final two teams.

        Args:
            n: The input number of teams in the tournament.

        Returns:
            The number of matches played in the tournament until the winner is decided.
        """
        return n - 1

    numberOfMatches = number_of_matches
