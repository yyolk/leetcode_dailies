# https://leetcode.com/problems/sudoku-solver/


class Solution:
    """37. Sudoku Solver

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy **all of the following rules**:

    1. Each of the digits `1-9` must occur exactly once in each row.

    2. Each of the digits `1-9` must occur exactly once in each column.

    3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes
    of the grid.

    The `'.'` character indicates empty cells."""

    def solve_sudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize boolean arrays to track used numbers in rows, columns, and 3x3 boxes
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Populate tracking arrays based on initial board values
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    idx = num - 1
                    rows[i][idx] = True
                    cols[j][idx] = True
                    box_id = (i // 3) * 3 + (j // 3)
                    boxes[box_id][idx] = True

        # Define recursive backtracking function starting at given row and column
        def solve(row: int, col: int) -> bool:
            # If reached end of grid, solution is found
            if row == 9:
                return True

            # Move to next row if at end of current row
            if col == 9:
                return solve(row + 1, 0)

            # Skip to next cell if current is already filled
            if board[row][col] != '.':
                return solve(row, col + 1)

            # Try numbers 1-9 in current empty cell
            for num in range(1, 10):
                idx = num - 1
                box_id = (row // 3) * 3 + (col // 3)
                # Check if number can be placed without violating rules
                if not rows[row][idx] and not cols[col][idx] and not boxes[box_id][idx]:
                    # Place number and update tracking
                    board[row][col] = str(num)
                    rows[row][idx] = True
                    cols[col][idx] = True
                    boxes[box_id][idx] = True
                    # Recurse to next cell; if successful, return True
                    if solve(row, col + 1):
                        return True
                    # Backtrack: remove number and reset tracking
                    board[row][col] = '.'
                    rows[row][idx] = False
                    cols[col][idx] = False
                    boxes[box_id][idx] = False

            # No valid number found, backtrack
            return False

        # Start solving from top-left cell
        solve(0, 0)

    solveSudoku = solve_sudoku