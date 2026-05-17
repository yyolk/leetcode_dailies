# https://leetcode.com/problems/pascals-triangle/


class Solution:
    """118. Pascal's Triangle

    Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

    In **Pascal's triangle**, each number is the sum of the two numbers directly above it as
    shown:

    ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
    """

    def generate(self, numRows: int) -> list[list[int]]:
        """Generate a Pascal Triangle, producing the rows requested.

        Proposed solution using nested for loops.
        As all elements need to be generated the time-complexity is `O(n^2)`.

        Args:
            numRows (int): the requested number of rows

        Returns:
            list of list of int: A 2D List consisting of every row in Pascal's triangle,
                index 0 is the top row
        """
        # Base list to hold the triangle's rows
        triangle = []

        for i in range(numRows):
            # Create an empty row to fill for every loop
            row = []
            for j in range(i + 1):
                # The first and last element per row in Pascal's triangle is always 1
                if j == 0 or j == i:
                    row.append(1)
                # Every other element is the sum of the two numbers directly above it
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)

        return triangle
