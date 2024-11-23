# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/


class Solution:
    """1072. Flip Columns For Maximum Number of Equal Rows

    You are given an `m x n` binary matrix `matrix`.

    You can choose any number of columns in the matrix and flip every cell in that
    column (i.e., Change the value of the cell from `0` to `1` or vice versa).

    Return *the maximum number of rows that have all values equal after some number of
    flips*.

    """

    def max_equal_rows_after_flips(self, matrix: list[list[int]]) -> int:
        # Dictionary to count occurrences of row patterns after potential flips
        pattern_count = {}

        for row in matrix:
            # If the first element is 1, we flip the entire row
            if row[0] == 1:
                pattern = tuple(0 if cell == 1 else 1 for cell in row)
            else:
                pattern = tuple(row)

            # Increment the count for this pattern or initialize if it's new
            pattern_count[pattern] = pattern_count.get(pattern, 0) + 1

        # Return the maximum number of equal rows after flipping
        return max(pattern_count.values()) if pattern_count else 0

    maxEqualRowsAfterFlips = max_equal_rows_after_flips
