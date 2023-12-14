# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/


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
        ...

    onesMinusZeros = ones_minus_zeros
