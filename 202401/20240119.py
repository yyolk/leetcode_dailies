# https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    """931. Minimum Falling Path Sum

    Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any
    **falling path** through* `matrix`.

    A **falling path** starts at any element in the first row and chooses the element in
    the next row that is either directly below or diagonally left/right. Specifically,
    the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1,
    col)`, or `(row + 1, col + 1)`.
    """

    def min_falling_path_sum(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Dynamic programming table to store minimum sum at each position
        dp = [[0] * cols for _ in range(rows)]

        # Copy the first row from the original matrix to the dp table
        for i in range(cols):
            dp[0][i] = matrix[0][i]

        # Iterate through the matrix starting from the second row
        for i in range(1, rows):
            for j in range(cols):
                # Calculate the minimum sum at each position
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][j],  # directly above
                    dp[i - 1][max(0, j - 1)],  # diagonally left
                    dp[i - 1][min(cols - 1, j + 1)]  # diagonally right
                )

        # Return the minimum sum from the last row of the dp table
        return min(dp[rows - 1])

    minFallingPathSum = min_falling_path_sum
