# https://leetcode.com/problems/first-completely-painted-row-or-column/


class Solution:
    """2661. First Completely Painted Row or Column

    You are given a **0-indexed** integer array `arr`, and an `m x n` integer **matrix**
    `mat`. `arr` and `mat` both contain **all** the integers in the range `[1, m * n]`.

    Go through each index `i` in `arr` starting from index `0` and paint the cell in
    `mat` containing the integer `arr[i]`.

    Return *the smallest index* `i` *at which either a row or a column will be
    completely painted in* `mat`."""

    def first_complete_index(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Dictionary to store positions of numbers in mat
        positions = {}
        for i in range(m):
            for j in range(n):
                positions[mat[i][j]] = (i, j)
        
        # Arrays to track painted cells in each row and column
        row_count = [0] * m
        col_count = [0] * n

        for i, num in enumerate(arr):
            row, col = positions[num]
            row_count[row] += 1
            col_count[col] += 1
            
            # Check if any row or column is completely painted
            if row_count[row] == n or col_count[col] == m:
                return i

        # This line should never be reached if inputs are valid
        return -1

    firstCompleteIndex = first_complete_index
