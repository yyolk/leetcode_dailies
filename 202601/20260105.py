# https://leetcode.com/problems/maximum-matrix-sum


class Solution:
    """1975. Maximum Matrix Sum

    You are given an n x n integer matrix. You can do the following
    operation any number of times:

    Choose any two adjacent elements of matrix and multiply each of them
    by -1.

    Two elements are considered adjacent if and only if they share a
    border.

    Your goal is to maximize the summation of the matrix's elements.
    Return the maximum sum of the matrix's elements using the operation
    mentioned above.
    """
    def max_matrix_sum(self, matrix: list[list[int]]) -> int:
        # Sum of absolute values (maximum possible if all non-negative)
        total_abs = 0
        # Minimum absolute value in the matrix
        # Initialized larger than any possible |val| per constraints
        min_abs_val = 100_001
        # Count of negative elements
        negative_count = 0

        # Single pass: compute total abs, min abs, and negative count
        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_abs += abs_val
                # Update min abs only if smaller
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
                if val < 0:
                    negative_count += 1

        # If even negatives: can make all non-negative
        # If has zero (min_abs_val == 0): can reduce odd negatives without penalty
        # Otherwise (odd negatives, no zero): must leave one negative,
        # choose the smallest abs to minimize the 2 * abs_val penalty
        if negative_count % 2 == 0 or min_abs_val == 0:
            return total_abs
        else:
            return total_abs - 2 * min_abs_val

    maxMatrixSum = max_matrix_sum