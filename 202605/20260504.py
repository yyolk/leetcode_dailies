# https://leetcode.com/problems/rotate-image/

class Solution:
    """48. Rotate Image
    
    You are given an n x n 2D matrix representing an image, rotate the image by 90
    degrees (clockwise). You have to rotate the image in-place, which means you
    have to modify the input 2D matrix directly. DO NOT allocate another 2D
    matrix and do the rotation.
    """
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # transpose: swap symmetric elements over main diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row for clockwise 90-degree rotation
        for row in matrix:
            row.reverse()

    rotate = rotate