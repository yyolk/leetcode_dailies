# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    """73. Set Matrix Zeroes

    Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row
    and column to `0`'s.

    You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).
    """

    def set_zeroes(self, matrix: list[list[int]]) -> None:
        # Get matrix dimensions
        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Check if first row and column contain any zeros
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 2: Use first row and column as markers for other zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Step 3: Set inner elements to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Set first row and column to zero if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

    setZeroes = set_zeroes
