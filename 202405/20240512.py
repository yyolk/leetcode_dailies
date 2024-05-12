# https://leetcode.com/problems/largest-local-values-in-a-matrix/


class Solution:
    """2373. Largest Local Values in a Matrix

    You are given an `n x n` integer matrix `grid`.

    Generate an integer matrix `maxLocal` of size `(n - 2) x (n - 2)` such that:

    * `maxLocal[i][j]` is equal to the **largest** value of the `3 x 3` matrix in `grid`
    centered around row `i + 1` and column `j + 1`.

    In other words, we want to find the largest value in every contiguous `3 x 3` matrix
    in `grid`.

    Return *the generated matrix*.

    """

    def largest_local(self, grid: list[list[int]]) -> list[list[int]]:
        # Check if grid is empty
        if not grid or not grid[0]:
            return []

        rows = len(grid)
        cols = len(grid[0])
        # Initialize maxLocal matrix with zeros
        max_local = [[0] * (cols - 2) for _ in range(rows - 2)]

        # Iterate over the inner portion of the grid to find local maximums
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                # Calculate local maximum within the 3x3 matrix
                local_max = max(
                    grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                    grid[i][j - 1], grid[i][j], grid[i][j + 1],
                    grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                )
                # Assign the local maximum to the corresponding position in maxLocal
                max_local[i - 1][j - 1] = local_max

        # Return the maxLocal matrix containing the largest local values
        return max_local

    largestLocal = largest_local
