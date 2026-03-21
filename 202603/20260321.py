# https://leetcode.com/problems/flip-square-submatrix-vertically

class Solution:
    """3643. Flip Square Submatrix Vertically

    You are given an m x n integer matrix grid, and three integers x, y, and k.
    The integers x and y represent the row and column indices of the top-left
    corner of a square submatrix and the integer k represents the size (side
    length) of the square submatrix.
    Your task is to flip the submatrix by reversing the order of its rows
    vertically.
    Return the updated matrix.
    """

    def reverse_submatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        for i in range(k // 2):
            # Swap row segments of the submatrix to reverse row order vertically
            # (middle row is untouched when k is odd)
            grid[x + i][y : y + k], grid[x + k - 1 - i][y : y + k] = (
                grid[x + k - 1 - i][y : y + k],
                grid[x + i][y : y + k],
            )
        return grid

    reverseSubmatrix = reverse_submatrix