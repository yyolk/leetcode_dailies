# https://leetcode.com/problems/maximal-rectangle


class Solution:
    """85. Maximal Rectangle

    Given a rows x cols binary matrix filled with 0's and 1's, find the largest
    rectangle containing only 1's and return its area.
    """
    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Update consecutive 1's heights for current row
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            # Monotonic stack to compute largest rectangle in histogram
            stack = [-1]  # Sentinel for left boundary
            for j in range(cols + 1):
                # Height drops to 0 at end of row
                h = heights[j] if j < cols else 0

                # Pop taller bars
                while stack[-1] != -1 and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]          # Height of popped bar
                    width = j - stack[-1] - 1              # Width bounded by left and right
                    max_area = max(max_area, height * width)

                if j < cols:
                    stack.append(j)

        return max_area

    maximalRectangle = maximal_rectangle