# https://leetcode.com/problems/largest-submatrix-with-rearrangements/


class Solution:
    """1727. Largest Submatrix With Rearrangements

    You are given a binary matrix `matrix` of size `m x n`, and you are allowed to
    rearrange the **columns** of the `matrix` in any order.

    Return *the area of the largest submatrix within* `matrix` *where **every** element
    of the submatrix is* `1` *after reordering the columns optimally.*
    """

    def largest_submatrix(self, matrix: list[list[int]]) -> int:
        """Find the area of the largest submatrix within the given matrix.

        Args:
            matrix: The input matrix as a 2D integer list.

        Returns:
            The area of the largest submatrix within the given input matrix.
        """
        m, n = len(matrix), len(matrix[0])

        max_area = 0

        # Calculate the cumulative sum for each column starting from the second row.
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j] if matrix[i][j] else 0

        # Sort each row in descending order and calculate the area for each row.
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                # Update the maximum area considering the current height and width.
                max_area = max(max_area, matrix[i][j] * (j + 1))

        return max_area

    largestSubmatrix = largest_submatrix
