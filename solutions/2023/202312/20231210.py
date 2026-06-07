# https://leetcode.com/problems/transpose-matrix/


class Solution:
    """867. Transpose Matrix

    Given a 2D integer array `matrix`, return *the **transpose** of* `matrix`.

    The **transpose** of a matrix is the matrix flipped over its main diagonal,
    switching the matrix's row and column indices.

    ![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)
    """

    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """Transpose the input matrix.

        Effectively transposes the matrix using `zip(...)`.

        Args:
            matrix: The input matrix.

        Returns:
            The transpose of the input matrix, aka the matrix flipped over its main
            diagonal.
        """
        # Use zip to unpack the rows of the matrix and repack those with the same index
        # into tuples. This effectively transposes the matrix.
        return list(map(list, zip(*matrix)))

    transpose = transpose
