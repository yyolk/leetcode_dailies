# https://leetcode.com/problems/magic-squares-in-grid/


class Solution:
    """840. Magic Squares In Grid

    A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from** 1
    **to** 9 such that each row, column, and both diagonals all have the same sum.

    Given a `row x col` `grid` of integers, how many `3 x 3` contiguous magic square
    subgrids are there?

    Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain
    numbers up to 15\\.

    """

    def num_magic_squares_inside(self, grid: list[list[int]]) -> int:
        def is_magic(square):
            # Check if the square contains all numbers from 1 to 9
            nums = [square[i][j] for i in range(3) for j in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False

            # Calculate row sums, column sums, and diagonal sums
            # First row sum
            sum1 = sum(square[0])
            # Second row sum
            sum2 = sum(square[1])
            # Third row sum
            sum3 = sum(square[2])
            # First column sum
            sum4 = sum(square[i][0] for i in range(3))
            # Second column sum
            sum5 = sum(square[i][1] for i in range(3))
            # Third column sum
            sum6 = sum(square[i][2] for i in range(3))
            # Main diagonal sum
            sum7 = sum(square[i][i] for i in range(3))
            # Anti-diagonal sum
            sum8 = sum(square[i][2 - i] for i in range(3))

            # All sums must be equal to 15
            return sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8 == 15

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                square = [grid[i + k][j : j + 3] for k in range(3)]
                if is_magic(square):
                    count += 1

        return count

    numMagicSquaresInside = num_magic_squares_inside
