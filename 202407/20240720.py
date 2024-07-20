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

    def restore_matrix(
        self, row_sum: list[int], col_sum: list[int]
    ) -> list[list[int]]: ...

    restoreMatrix = restore_matrix
