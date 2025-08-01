# https://leetcode.com/problems/pascals-triangle/


class Solution:
    """118. Pascal's Triangle

    Given an integer `num_rows`, return the first num_rows of **Pascal's triangle**.

    In **Pascal's triangle**, each number is the sum of the two numbers directly above
    it as shown:

    ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
    """

    def generate(self, num_rows: int) -> list[list[int]]:
        if num_rows == 0:
            return []
        result = [[1]]
        for i in range(1, num_rows):
            new_row = [1]
            for j in range(1, i):
                new_row.append(result[i - 1][j - 1] + result[i - 1][j])
            new_row.append(1)
            result.append(new_row)
        return result