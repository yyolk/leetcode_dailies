# https://leetcode.com/problems/maximal-rectangle/


class Solution:
    """85. Maximal Rectangle

    Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest
    rectangle containing only `1`'s and return *its area*.

    """

    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            max_area = max(max_area, self.largest_rectangle_area(heights))

        return max_area

    def largest_rectangle_area(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        # Adding a 0 at the end to clear the stack at the end
        heights.append(0)

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area

    maximalRectangle = maximal_rectangle
