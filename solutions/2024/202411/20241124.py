# https://leetcode.com/problems/maximum-matrix-sum/


class Solution:
    """1975. Maximum Matrix Sum

    You are given an `n x n` integer `matrix`. You can do the following operation
    **any** number of times:

    * Choose any two **adjacent** elements of `matrix` and **multiply** each of them by
    `-1`.

    Two elements are considered **adjacent** if and only if they share a **border**.

    Your goal is to **maximize** the summation of the matrix's elements. Return *the
    **maximum** sum of the matrix's elements using the operation mentioned above.*

    """

    def max_matrix_sum(self, matrix: list[list[int]]) -> int:
        # Flatten the matrix to work with a single list
        flat = [num for row in matrix for num in row]

        # Count of negative numbers
        neg_count = sum(1 for num in flat if num < 0)

        # Calculate the absolute sum
        abs_sum = sum(abs(num) for num in flat)

        # If there's an odd number of negatives, we need to subtract twice the smallest absolute value
        # because we'll flip this one to positive, reducing the sum by 2*abs(min value)
        if neg_count % 2 == 1:
            min_abs = min(abs(num) for num in flat)
            return abs_sum - 2 * min_abs
        else:
            # If even number of negatives or all positives, just return the absolute sum
            return abs_sum

    maxMatrixSum = max_matrix_sum
