# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/


class Solution:
    """1074. Number of Submatrices That Sum to Target

    Given a `matrix` and a `target`, return the number of non-empty submatrices that sum
    to target.

    A submatrix `x1, y1, x2, y2` is the set of all cells `matrix[x][y]` with `x1 <= x <=
    x2` and `y1 <= y <= y2`.

    Two submatrices `(x1, y1, x2, y2)` and `(x1', y1', x2', y2')` are different if they
    have some coordinate that is different: for example, if `x1 != x1'`.

    """

    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int: ...

    numSubmatrixSumTarget = num_submatrix_sum_target
