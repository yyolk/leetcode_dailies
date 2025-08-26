# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/


class Solution:
    """3000. Maximum Area of Longest Diagonal Rectangle

    You are given a 2D **0-indexed** integer array `dimensions`.

    For all indices `i`, `0 <= i < dimensions.length`, `dimensions[i][0]` represents the
    length and `dimensions[i][1]` represents the width of the rectangle `i`.

    Return *the **area** of the rectangle having the **longest** diagonal. If there are
    multiple rectangles with the longest diagonal, return the area of the rectangle
    having the **maximum** area.*"""

    def area_of_max_diagonal(self, dimensions: list[list[int]]) -> int:
        # Initialize max diagonal squared and max area
        max_diag_sq = 0
        max_area = 0
        for rect in dimensions:
            l, w = rect
            # Compute diagonal squared to avoid floating point
            diag_sq = l * l + w * w
            # Compute area
            area = l * w
            if diag_sq > max_diag_sq:
                # Update for longer diagonal
                max_diag_sq = diag_sq
                max_area = area
            elif diag_sq == max_diag_sq:
                # For same diagonal, take larger area
                max_area = max(max_area, area)
        return max_area

    areaOfMaxDiagonal = area_of_max_diagonal
