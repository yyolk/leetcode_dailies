# https://leetcode.com/problems/find-the-winner-of-an-array-game/


class Solution:
    """1535. Find the Winner of an Array Game

    Given an integer array `arr` of **distinct** integers and an integer `k`.

    A game will be played between the first two elements of the array (i.e. `arr[0]` and
    `arr[1]`). In each round of the game, we compare `arr[0]` with `arr[1]`, the larger
    integer wins and remains at position `0`, and the smaller integer moves to the end
    of the array. The game ends when an integer wins `k` consecutive rounds.

    Return *the integer which will win the game*.

    It is **guaranteed** that there will be a winner of the game.
    """

    def get_winner(self, arr: list[int], k: int) -> int:
        """Find the winner of the array game after k consecutive wins.

        Proposed solution by simulating the game.

        Args:
            arr: A list of distinct integers.
            k: An integer representing the number of consecutive rounds to win.

        Returns:
            The integer that will win the game after k consecutive wins.
        """
        # Handle edge cases and be efficient.
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)

        # Initialize the consecutive wins counter and the winner.
        consecutive_wins = 0
        winner = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1

            if consecutive_wins == k:
                return winner

        return winner

    getWinner = get_winner
