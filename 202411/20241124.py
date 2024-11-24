# https://leetcode.com/problems/maximum-matrix-sum/


class Solution:
    """1975. Maximum Matrix Sum

    You are given an `n x n` integer `matrix`. You can do the following operation
    **any** number of times:

    * Choose any two **adjacent** elements of `matrix` and **multiply** each of them by
    `-1`.

    Two elements are considered **adjacent** if and only if they share a **border**.

    Your goal is to **maximize** the summation of the matrix's elements. Return *the
    **maximum** sum of the matrix's elements using the operation mentioned above.*

    """

    def max_matrix_sum(self, matrix: list[list[int]]) -> int: ...

    maxMatrixSum = max_matrix_sum
