# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
from collections import Counter
from itertools import groupby


class Solution:
    """2038. Remove Colored Pieces if Both Neighbors are the Same Color

    There are `n` pieces arranged in a line, and each piece is colored either by `'A'` or by
    `'B'`. You are given a string `colors` of length `n` where `colors[i]` is the color of
    the `ith` piece.

    Alice and Bob are playing a game where they take **alternating turns** removing pieces
    from the line. In this game, Alice moves **first**.

    * Alice is only allowed to remove a piece colored `'A'` if **both its neighbors** are
    also colored `'A'`. She is **not allowed** to remove pieces that are colored `'B'`.

    * Bob is only allowed to remove a piece colored `'B'` if **both its neighbors** are also
    colored `'B'`. He is **not allowed** to remove pieces that are colored `'A'`.

    * Alice and Bob **cannot** remove pieces from the edge of the line.

    * If a player cannot make a move on their turn, that player **loses** and the other
    player **wins**.

    Assuming Alice and Bob play optimally, return `true` *if Alice wins, or return* `false`
    *if Bob wins*.
    """

    def winnerOfGame(self, colors: str) -> bool:
        """Finds the winner of the game between Alice and Bob

        Proposed solution, using collections.Counter and itertools.groupby to pull
        out consecutive pieces and then increment the counter if there's two neighbors.

        Args:
            colors (str): The input colors string which map to the intials of
            Alice, 'A' or Bob, 'B'.

        Returns:
            bool: True if Alice wins, False if Bob wins.
        """
        # Initialize a Counter for storing moves for Alice and Bob
        moves_counter = Counter()

        # Group consecuritve identical characters using groupby
        for x, t in groupby(colors):
            # Increment the moves counter if there are two consecutive neighbors of
            # the same color
            moves_counter[x] += max(len(list(t)) - 2, 0)

        # If Alice has more moves than Bob, Alice wins.
        if moves_counter["A"] > moves_counter["B"]:
            return True
        # Bob wins by default
        return False
