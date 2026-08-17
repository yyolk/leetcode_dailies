# https://leetcode.com/problems/stone-game-v/


class Solution:
    """1563. Stone Game V

    There are several stones **arranged in a row**, and each stone has an associated
    value which is an integer given in the array `stone_value`.

    In each round of the game, Alice divides the row into **two non-empty rows** (i.e.
    left row and right row), then Bob calculates the value of each row which is the sum
    of the values of all the stones in this row. Bob throws away the row which has the
    maximum value, and Alice's score increases by the value of the remaining row. If the
    value of the two rows are equal, Bob lets Alice decide which row will be thrown
    away. The next round starts with the remaining row.

    The game ends when there is only **one stone remaining**. Alice's score is initially
    **zero**.

    Return *the maximum score that Alice can obtain*.

    Constraints:

    * `1 <= stone_value.length <= 500`

    * `1 <= stone_value[i] <= 106`"""

    def stone_game_v(self, stone_value: list[int]) -> int:
        """Return the maximum score Alice can obtain."""
        n = len(stone_value)
        if n == 1:
            return 0

        prefix = [0] * (n + 1)
        for i, value in enumerate(stone_value):
            prefix[i + 1] = prefix[i] + value

        dp = [[0] * n for _ in range(n)]
        best_left = [[0] * n for _ in range(n)]
        best_right = [[0] * n for _ in range(n)]

        for i, value in enumerate(stone_value):
            best_left[i][i] = value
            best_right[i][i] = value

        for left in range(n - 1, -1, -1):
            mid = left
            for right in range(left + 1, n):
                total = prefix[right + 1] - prefix[left]

                while (
                    mid < right
                    and (prefix[mid + 1] - prefix[left]) * 2 < total
                ):
                    mid += 1

                best = 0
                if left <= mid - 1:
                    best = max(best, best_left[left][mid - 1])
                if mid + 1 <= right:
                    best = max(best, best_right[mid + 1][right])
                if (prefix[mid + 1] - prefix[left]) * 2 == total:
                    best = max(best, best_left[left][mid])

                dp[left][right] = best
                score_with_total = best + total
                best_left[left][right] = max(
                    best_left[left][right - 1], score_with_total
                )
                best_right[left][right] = max(
                    best_right[left + 1][right], score_with_total
                )

        return dp[0][n - 1]

    stoneGameV = stone_game_v
