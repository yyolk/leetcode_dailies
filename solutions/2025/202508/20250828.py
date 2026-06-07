# https://leetcode.com/problems/sort-matrix-by-diagonals/


class Solution:
    """3446. Sort Matrix by Diagonals

    You are given an `n x n` square matrix of integers `grid`. Return the matrix such
    that:

    * The diagonals in the **bottom-left triangle** (including the middle diagonal) are
    sorted in **non-increasing order**.

    * The diagonals in the **top-right triangle** are sorted in **non-decreasing
    order**."""

    def sort_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        # Get the size of the matrix
        n = len(grid)
        # Iterate over all possible diagonals, where d = i - j ranges from -(n-1) to (n-1)
        for d in range(-(n - 1), n):
            # Calculate the starting row index: max(0, d) to handle upper and lower bounds
            start_i = max(0, d)
            # Calculate the ending row index (exclusive): min(n, n + d) to stay within matrix limits
            end_i = min(n, n + d)
            # Collect elements on the diagonal in order of increasing row i
            diag = [grid[i][i - d] for i in range(start_i, end_i)]
            # Sort based on triangle: d >= 0 for bottom-left (non-increasing), d < 0 for top-right (non-decreasing)
            if d >= 0:
                # Sort in descending order for non-increasing
                diag.sort(reverse=True)
            else:
                # Sort in ascending order for non-decreasing
                diag.sort()
            # Place sorted elements back into the grid in the same order
            for idx, i in enumerate(range(start_i, end_i)):
                grid[i][i - d] = diag[idx]
        # Return the modified grid
        return grid

    sortMatrix = sort_matrix
