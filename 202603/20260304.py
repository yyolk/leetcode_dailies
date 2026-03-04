# https://leetcode.com/problems/special-positions-in-a-binary-matrix

class Solution:
    """1582. Special Positions in a Binary Matrix
    
    Given an m x n binary matrix mat, return the number of special positions in
    mat. A position (i, j) is called special if mat[i][j] == 1 and all other
    elements in row i and column j are 0 (rows and columns are 0-indexed).
    """
    def num_special(self, mat: list[list[int]]) -> int:
        # get matrix dimensions (handle empty matrix safely)
        rows = len(mat)
        cols = len(mat[0]) if mat else 0

        # count number of 1s for each row and each column
        row_count = [0] * rows
        col_count = [0] * cols

        # first pass: populate row and column counts only where value is 1
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # second pass: count special positions
        special_count = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1

        return special_count

    numSpecial = num_special