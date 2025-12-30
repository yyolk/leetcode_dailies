# https://leetcode.com/problems/magic-squares-in-grid/


class Solution:
    """840. Magic Squares In Grid

    A 3x3 magic square is a 3x3 grid filled with distinct numbers from 1 to 9
    such that each row, column, and both main diagonals have the same sum.

    Given a row x col grid of integers, count how many 3x3 magic square
    subgrids it contains.

    Note: grid may contain numbers up to 15.
    """
    def num_magic_squares_inside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        count = 0
        # Iterate over all possible top-left corners of 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                # Extract the 3x3 subgrid as list of rows
                square = [grid[i + k][j:j + 3] for k in range(3)]
                if self._is_magic(square):
                    count += 1
        return count

    def _is_magic(self, square: list[list[int]]) -> bool:
        # Flatten to check for distinct 1-9
        nums = [square[x][y] for x in range(3) for y in range(3)]
        if sorted(nums) != list(range(1, 10)):
            return False

        # Magic constant must be 15 for numbers 1-9
        magic = 15

        # Check all row sums
        if sum(square[0]) != magic or sum(square[1]) != magic or sum(square[2]) != magic:
            return False

        # Check all column sums
        for c in range(3):
            if square[0][c] + square[1][c] + square[2][c] != magic:
                return False

        # Check main diagonal
        if square[0][0] + square[1][1] + square[2][2] != magic:
            return False

        # Check anti-diagonal
        if square[0][2] + square[1][1] + square[2][0] != magic:
            return False

        return True

    numMagicSquaresInside = num_magic_squares_inside