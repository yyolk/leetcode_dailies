# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
from functools import cache


class Solution:
    """1931. Painting a Grid With Three Different Colors

    You are given two integers `m` and `n`. Consider an `m x n` grid where each cell is
    initially white. You can paint each cell **red**, **green**, or **blue**. All cells
    **must** be painted.

    Return *the number of ways to color the grid with **no two adjacent cells having the
    same color***. Since the answer can be very large, return it **modulo** `109 + 7`.
    """

    def color_the_grid(self, m: int, n: int) -> int:
        # Note: Here, m is the number of columns, n is the number of rows
        @cache
        def generate_valid_rows(previous_row):
            # Generate all possible valid colorings for the current row based on the previous row
            def build_row(col_idx, current_row):
                # If the entire row is colored (all columns filled), return it as a list
                if col_idx == m:
                    return [current_row]
                # Try each color and recursively build the rest of the row
                return sum(
                    (
                        build_row(col_idx + 1, current_row + color)
                        for color in "rgb"
                        if previous_row[col_idx] != color
                        and (col_idx == 0 or current_row[-1] != color)
                    ),
                    [],
                )

            # Start building the row from column 0 with an empty string
            return build_row(0, "")

        @cache
        def count_ways(row_idx, previous_row):
            # Count the number of ways to color the grid starting from the current row
            if row_idx == n:
                # All rows have been colored, this is a valid configuration
                return 1
            # Sum the number of ways for each valid coloring of the current row
            return sum(
                count_ways(row_idx + 1, current_row)
                for current_row in generate_valid_rows(previous_row)
            ) % (10**9 + 7)

        # Begin with row 0 and a dummy previous row of underscores (no constraints)
        return count_ways(0, "_" * m)

    colorTheGrid = color_the_grid
