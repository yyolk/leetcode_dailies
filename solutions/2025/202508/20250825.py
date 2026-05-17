# https://leetcode.com/problems/diagonal-traverse/


class Solution:
    """498. Diagonal Traverse

    Given an `m x n` matrix `mat`, return *an array of all the elements of the array in
    a diagonal order*."""

    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            # Handle empty matrix
            return []

        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of columns

        result = []  # List to store the diagonal traversal

        # Iterate over each diagonal, where d = i + j ranges from 0 to m+n-2
        for d in range(m + n - 1):
            diagonal = []  # Temporary list for current diagonal elements

            # Calculate starting row for this diagonal
            start_row = max(0, d - n + 1)
            # Calculate ending row for this diagonal
            end_row = min(d, m - 1)

            # Collect elements in the diagonal, increasing row i, decreasing column j
            for i in range(start_row, end_row + 1):
                j = d - i
                diagonal.append(mat[i][j])

            # For even d, reverse the diagonal (down-left to up-right direction)
            # For odd d, keep as is (up-right to down-left direction)
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result

    findDiagonalOrder = find_diagonal_order
