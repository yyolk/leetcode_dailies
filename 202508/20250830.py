# https://leetcode.com/problems/valid-sudoku/


class Solution:
    """36. Valid Sudoku

    Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be
    validated **according to the following rules**:

    1. Each row must contain the digits `1-9` without repetition.

    2. Each column must contain the digits `1-9` without repetition.

    3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9`
    without repetition.

    **Note:**

    * A Sudoku board (partially filled) could be valid but is not necessarily solvable.

    * Only the filled cells need to be validated according to the mentioned rules."""

    def is_valid_sudoku(self, board: list[list[str]]) -> bool: ...

    isValidSudoku = is_valid_sudoku
