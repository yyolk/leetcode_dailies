# https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    """119. Pascal's Triangle II

    Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed**) row of the
    **Pascal's triangle**.

    In **Pascal's triangle**, each number is the sum of the two numbers directly above
    it as shown:

    ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
    """

    def get_row(self, row_index: int) -> List[int]:
        """Gets the row from the computed Pascal's Triangle.

        Proposed solution.

        Args:
            row_index (int): Which row to get, 0-indexed, starting from the top.

        Returns:
            List of int: The requested row of numbers in Pascal's Triangle.
        """
        # Initialize the first row
        row = [1]

        for i in range(1, row_index + 1):
            # Create a new row
            new_row = [1]
            for j in range(1, i):
                # Calculate the next value using the previous row
                new_value = row[j - 1] + row[j]
                new_row.append(new_value)

            # Add the final 1 (right most value) to the new row
            new_row.append(1)

            # Update the current row
            row = new_row

        # We've reached our requested index, return the row
        return row

    getRow = get_row
