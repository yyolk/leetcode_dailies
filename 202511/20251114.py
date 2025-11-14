# https://leetcode.com/problems/increment-submatrices-by-one/


class Solution:
    """2536. Increment Submatrices by One

    You are given a positive integer n, indicating that we initially have an
    n x n 0-indexed integer matrix mat filled with zeroes.

    You are also given a 2D integer array query. For each query[i] =
    [row1i, col1i, row2i, col2i], you should do the following operation:

    Add 1 to every element in the submatrix with the top left corner
    (row1i, col1i) and the bottom right corner (row2i, col2i). That is,
    add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.

    Return the matrix mat after performing every query.
    """
    def range_add_queries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        # Initialize the difference array of size (n+1) x (n+1)
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        # Apply each query to the difference array
        for query in queries:
            r1, c1, r2, c2 = query
            # Increment top-left corner
            diff[r1][c1] += 1
            # Decrement top-right (column end)
            diff[r1][c2 + 1] -= 1
            # Decrement bottom-left (row end)
            diff[r2 + 1][c1] -= 1
            # Increment bottom-right (to cancel out the double decrement)
            diff[r2 + 1][c2 + 1] += 1
        # Compute the prefix sums in place to get the final values
        for i in range(n):
            for j in range(n):
                # Add value from above cell
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                # Add value from left cell
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                # Subtract the diagonal to avoid double counting
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
        # Extract the n x n matrix from the diff array
        return [row[:n] for row in diff[:n]]

    rangeAddQueries = range_add_queries