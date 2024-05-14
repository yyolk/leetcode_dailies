# https://leetcode.com/problems/score-after-flipping-matrix/


class Solution:
    """861. Score After Flipping Matrix

    You are given an `m x n` binary matrix `grid`.

    A **move** consists of choosing any row or column and toggling each value in that
    row or column (i.e., changing all `0`'s to `1`'s, and all `1`'s to `0`'s).

    Every row of the matrix is interpreted as a binary number, and the **score** of the
    matrix is the sum of these numbers.

    Return *the highest possible **score** after making any number of **moves**
    (including zero moves)*.

    """

    def matrix_score(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Greedily toggle rows to ensure the leftmost bit is always 1
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] ^= 1  # Toggle the bit

        # Greedily toggle columns to maximize the score
        score = 0
        for j in range(1, cols):  # Start from the second column
            count_ones = sum(grid[i][j] for i in range(rows))
            score += max(count_ones, rows - count_ones) * (2 ** (cols - j - 1))

        # Add the score from the first column
        score += rows * (2 ** (cols - 1))

        return score

    matrixScore = matrix_score
