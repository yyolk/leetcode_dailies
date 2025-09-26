# https://leetcode.com/problems/triangle/


class Solution:
    """120. Triangle

    Given a `triangle` array, return *the minimum path sum from top to bottom*.

    For each step, you may move to an adjacent number of the row below. More formally,
    if you are on index `i` on the current row, you may move to either index `i` or
    index `i + 1` on the next row."""

    def minimum_total(self, triangle: list[list[int]]) -> int:
        # Get the number of rows in the triangle
        n = len(triangle)
        # If the triangle is empty, return 0 (though problem assumes at least one row)
        if n == 0:
            return 0
        # Start from the second last row and move upwards
        for row in range(n - 2, -1, -1):
            # For each position in the current row
            for col in range(row + 1):
                # Add the minimum of the two adjacent values from the row below
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )
        # The top element now holds the minimum path sum
        return triangle[0][0]

    minimumTotal = minimum_total
