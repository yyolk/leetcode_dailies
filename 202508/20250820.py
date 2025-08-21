# https://leetcode.com/problems/count-square-submatrices-with-all-ones/


class Solution:
    """1277. Count Square Submatrices with All Ones

    Given a `m * n` matrix of ones and zeros, return how many **square** submatrices
    have all ones."""

    def count_squares(self, matrix: list[list[int]]) -> int:
        # Handle empty matrix cases
        if not matrix or not matrix[0]:
            return 0

        # Get matrix dimensions
        m, n = len(matrix), len(matrix[0])

        # Initialize DP table where dp[i][j] will store the size of the largest square ending at (i, j)
        dp = [[0] * n for _ in range(m)]

        # Variable to accumulate the total count of squares
        total = 0

        # Iterate over each cell in the matrix
        for i in range(m):
            for j in range(n):
                # Skip if cell is 0, as no square can end here
                if matrix[i][j] == 0:
                    continue

                # For border cells, the square size is 1 if cell is 1
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # Compute square size as 1 plus min of top, left, and top-left DP values
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                # Add the number of squares ending at this cell (sizes 1 to dp[i][j])
                total += dp[i][j]

        # Return the total count
        return total

    countSquares = count_squares
