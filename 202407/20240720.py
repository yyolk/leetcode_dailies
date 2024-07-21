# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/


class Solution:
    """1605. Find Valid Matrix Given Row and Column Sums

    You are given two arrays `row_sum` and `col_sum` of non\\-negative integers where
    `row_sum[i]` is the sum of the elements in the `ith` row and `col_sum[j]` is the sum
    of the elements of the `jth` column of a 2D matrix. In other words, you do not know
    the elements of the matrix, but you do know the sums of each row and column.

    Find any matrix of **non\\-negative** integers of size `row_sum.length x
    col_sum.length` that satisfies the `row_sum` and `col_sum` requirements.

    Return *a 2D array representing **any** matrix that fulfills the requirements*. It's
    guaranteed that **at least one** matrix that fulfills the requirements exists.

    """

    def restore_matrix(self, row_sum: list[int], col_sum: list[int]) -> list[list[int]]:
        # Initialize the result matrix with zeroes
        m, n = len(row_sum), len(col_sum)
        result = [[0] * n for _ in range(m)]

        # Iterate through each cell and fill it with the minimum of the current row_sum and col_sum
        for i in range(m):
            for j in range(n):
                # Find the minimum of the current row_sum and col_sum
                min_val = min(row_sum[i], col_sum[j])

                # Fill the cell with min_val
                result[i][j] = min_val

                # Subtract the filled value from the corresponding row_sum and col_sum
                row_sum[i] -= min_val
                col_sum[j] -= min_val

                # If either the row_sum or col_sum is zero, move to the next row or column
                if row_sum[i] == 0:
                    break
            if row_sum[i] == 0:
                continue

        return result

    restoreMatrix = restore_matrix
