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
        """...

        Proposed solution ...

        Args:
            stone_value (list of int): ...

        Returns:
            int: ..."""
        ...

    stoneGameV = stone_game_v
