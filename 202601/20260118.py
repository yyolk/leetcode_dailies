# https://leetcode.com/problems/largest-magic-square


class Solution:
    """1895. Largest Magic Square

    A k x k magic square is a k x k grid filled with integers such that
    every row sum, every column sum, and both diagonal sums are all
    equal. The integers in the magic square do not have to be distinct.
    Every 1 x 1 grid is trivially a magic square.

    Given an m x n integer grid, return the size (i.e., the side length k)
    of the largest magic square that can be found within this grid.
    """
    def largest_magic_square(self, grid: list[list[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        # Precompute prefix sums for fast row range queries
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]

        # Precompute prefix sums for fast column range queries
        col_prefix = [[0] * (m + 1) for _ in range(n)]
        for j in range(n):
            for i in range(m):
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]

        # Check from largest possible k down to 2 (k=1 always valid)
        for k in range(min(m, n), 1, -1):
            for start_row in range(m - k + 1):
                for start_col in range(n - k + 1):
                    # Use first row sum as candidate magic constant
                    magic = (row_prefix[start_row][start_col + k] -
                             row_prefix[start_row][start_col])

                    # Verify all other row sums match magic
                    rows_match = True
                    for r in range(start_row + 1, start_row + k):
                        if (row_prefix[r][start_col + k] -
                                row_prefix[r][start_col]) != magic:
                            rows_match = False
                            break
                    if not rows_match:
                        continue

                    # Verify all column sums match magic
                    cols_match = True
                    for c in range(start_col, start_col + k):
                        col_sum = (col_prefix[c][start_row + k] -
                                   col_prefix[c][start_row])
                        if col_sum != magic:
                            cols_match = False
                            break
                    if not cols_match:
                        continue

                    # Verify main diagonal sum
                    diag1 = 0
                    for d in range(k):
                        diag1 += grid[start_row + d][start_col + d]
                    if diag1 != magic:
                        continue

                    # Verify anti-diagonal sum
                    diag2 = 0
                    for d in range(k):
                        diag2 += grid[start_row + d][start_col + k - 1 - d]
                    if diag2 != magic:
                        continue

                    # All conditions satisfied
                    return k

        return 1

    largestMagicSquare = largest_magic_square