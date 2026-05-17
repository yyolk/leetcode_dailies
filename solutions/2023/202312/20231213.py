# https://leetcode.com/problems/special-positions-in-a-binary-matrix/


class Solution:
    """1582. Special Positions in a Binary Matrix

    Given an `m x n` binary matrix `mat`, return *the number of special positions in*
    `mat`*.*

    A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements
    in row `i` and column `j` are `0` (rows and columns are **0-indexed**).
    """

    def num_special(self, mat: list[list[int]]) -> int:
        """Number of special position in input matrix.

        Args:
            mat: The input matrix to search.

        Returns:
            The number of special positions in the input matrix.
        """
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        special_count = 0

        # Count the number of 1s in each row and column.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Check for special_count.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1

        return special_count

    numSpecial = num_special
