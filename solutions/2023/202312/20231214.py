# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
import numpy as np


class Solution:
    """2482. Difference Between Ones and Zeros in Row and Column

    You are given a **0-indexed** `m x n` binary matrix `grid`.

    A **0-indexed** `m x n` difference matrix `diff` is created with the following
    procedure:

    * Let the number of ones in the `ith` row be `onesRowi`.

    * Let the number of ones in the `jth` column be `onesColj`.

    * Let the number of zeros in the `ith` row be `zerosRowi`.

    * Let the number of zeros in the `jth` column be `zerosColj`.

    * `diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj`

    Return *the difference matrix* `diff`.
    """

    def ones_minus_zeros(self, grid: list[list[int]]) -> list[list[int]]:
        """Find the differences of ones and zeroes for all columns and rows.

        Args:
            grid: The input 2D list of integers (matrix) to summate columns and rows.

        Returns:
            The calculated 2D integer list of all rows and columns summated in the last
            row and last column.
        """
        # Convert the grid into a numpy array.
        grid_np = np.array(grid)

        # Get the grid dimensions.
        m, n = grid_np.shape

        # Calculate the sum of ones in each row and column.
        ones_row = np.sum(grid_np, axis=1)
        ones_col = np.sum(grid_np, axis=0)

        # Calculate the sum of zeros in each row and column.
        zeroes_row = n - ones_row
        zeroes_col = m - ones_col

        # Calculate the difference matrix using broadcasting.
        diff = (
            ones_row[:, np.newaxis] + ones_col - zeroes_row[:, np.newaxis] - zeroes_col
        )

        # Convert the numpy array back into a list, the expected output.
        return diff.tolist()

    onesMinusZeros = ones_minus_zeros
