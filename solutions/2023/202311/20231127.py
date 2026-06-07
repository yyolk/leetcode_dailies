# https://leetcode.com/problems/knight-dialer/
MOD = 10**9 + 7


class Solution:
    """935. Knight Dialer

    The chess knight has a **unique movement**, it may move two squares vertically and
    one square horizontally, or two squares horizontally and one square vertically (with
    both forming the shape of an **L**). The possible movements of chess knight are
    shown in this diagaram:

    A chess knight can move as indicated in the chess diagram below:

    ![](https://assets.leetcode.com/uploads/2020/08/18/chess.jpg)

    We have a chess knight and a phone pad as shown below, the knight **can only stand
    on a numeric cell** (i.e. blue cell).

    ![](https://assets.leetcode.com/uploads/2020/08/18/phone.jpg)

    Given an integer `n`, return how many distinct phone numbers of length `n` we can
    dial.

    You are allowed to place the knight **on any numeric cell** initially and then you
    should perform `n - 1` jumps to dial a number of length `n`. All jumps should be
    **valid** knight jumps.

    As the answer may be very large, **return the answer modulo** `109 + 7`.
    """

    def knight_dialer(self, n: int) -> int:
        """How many distinct numbers of length n can be dialed using a Knight's movement.

        10 is the maximum number of digits in a phone number.

        Args:
            n: The target length of distinct sequence of digits that will form a number.

        Returns:
            The number of distinct numbers that can be dialed, trimmed to MOD.
        """
        max_number_length = 10
        # Create a moves lookup table, where the knight can move from from starting key.
        moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        # Initialize a 2D array dp where dp[i][j] represents the number of ways to reach
        # digit j with i moves.
        dp = [[0] * max_number_length for _ in range(n)]

        # Initialize the base case: with 1 move, there is only 1 way to reach each digit.
        for i in range(max_number_length):
            dp[0][i] = 1

        # Populate the dp array using th eknight's moves.
        for i in range(1, n):
            for j in range(max_number_length):
                # The number of ways to reach digit j with i moves is the sum of ways
                # to reach the next_digit from the moves[j] list with i-1 moves.
                dp[i][j] = sum(dp[i - 1][next_digit] for next_digit in moves[j]) % MOD

        # Sum up the possibilities for all digits with n moves.
        return sum(dp[n - 1]) % MOD

    knightDialer = knight_dialer
