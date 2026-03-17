# https://leetcode.com/problems/largest-submatrix-with-rearrangements

class Solution:
    """1727. Largest Submatrix With Rearrangements
    
    You are given a binary matrix matrix of size m x n, and you are allowed to
    rearrange the columns of the matrix in any order.
    Return the area of the largest submatrix within matrix where every element of
    the submatrix is 1 after reordering the columns optimally.
    """
    def largest_submatrix(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        # Number of columns
        n = len(matrix[0])
        # heights tracks consecutive 1s ending at current row for each column
        heights = [0] * n
        max_area = 0
        for row in matrix:
            # Update consecutive heights
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] else 0
            # Sort heights descending to simulate optimal column rearrangement
            sorted_heights = sorted(heights, reverse=True)
            # For width (k+1), use the (k)-th largest height
            for k in range(n):
                max_area = max(max_area, sorted_heights[k] * (k + 1))
        return max_area

    largestSubmatrix = largest_submatrix