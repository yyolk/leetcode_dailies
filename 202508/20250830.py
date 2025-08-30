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

    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        # Initialize sets for rows, columns, and 3x3 boxes to track seen numbers
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        
        # Iterate over each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                # Skip empty cells marked with "."
                if num == ".":
                    continue
                
                # Check for duplicate in the current row
                if num in row_sets[i]:
                    return False
                row_sets[i].add(num)
                
                # Check for duplicate in the current column
                if num in col_sets[j]:
                    return False
                col_sets[j].add(num)
                
                # Calculate the index for the 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                # Check for duplicate in the current box
                if num in box_sets[box_index]:
                    return False
                box_sets[box_index].add(num)
        
        # If no duplicates found in rows, columns, or boxes, the board is valid
        return True

    isValidSudoku = is_valid_sudoku
