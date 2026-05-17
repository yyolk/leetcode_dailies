# https://leetcode.com/problems/count-square-submatrices-with-all-ones/


class Solution:
    """1277. Count Square Submatrices with All Ones

    Given a `m * n` matrix of ones and zeros, return how many **square** submatrices
    have all ones.

    """

    def count_squares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # dp[i][j] represents the side length of the largest square
        # whose bottom-right corner is at (i, j)
        dp = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # If it's on the edge or if it's 1, determine the size:
                    # - If it's on the first row or column, it can only be 1
                    # - Otherwise, it's the min of the three adjacent squares plus one
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    # Add the size of this square to our count
                    count += dp[i][j]

        return count

    countSquares = count_squares
