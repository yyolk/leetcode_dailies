# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/


class Solution:
    """3197. Find the Minimum Area to Cover All Ones II

    You are given a 2D **binary** array `grid`. You need to find 3 **non-overlapping**
    rectangles having **non-zero** areas with horizontal and vertical sides such that
    all the 1's in `grid` lie inside these rectangles.

    Return the **minimum** possible sum of the area of these rectangles.

    **Note** that the rectangles are allowed to touch."""

    def minimum_sum(self, grid: list[list[int]]) -> int:
        import math
        m = len(grid)
        n = len(grid[0])
        # Initialize answer to a large value, the total grid area
        ans = m * n

        # Case 1: Top horizontal rectangle, bottom split into left and right vertical rectangles
        for i in range(m):
            top = self._minimumArea(grid, 0, i, 0, n - 1)
            for j in range(n):
                left = self._minimumArea(grid, i + 1, m - 1, 0, j)
                right = self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1)
                # Only consider if all three rectangles have positive area
                if top > 0 and left > 0 and right > 0:
                    ans = min(ans, top + left + right)

        # Case 2: Bottom horizontal rectangle, top split into left and right vertical rectangles
        for i in range(m):
            bottom = self._minimumArea(grid, i, m - 1, 0, n - 1)
            for j in range(n):
                left = self._minimumArea(grid, 0, i - 1, 0, j)
                right = self._minimumArea(grid, 0, i - 1, j + 1, n - 1)
                # Only consider if all three rectangles have positive area
                if bottom > 0 and left > 0 and right > 0:
                    ans = min(ans, bottom + left + right)

        # Case 3: Left vertical rectangle, right split into top and bottom horizontal rectangles
        for j in range(n):
            left = self._minimumArea(grid, 0, m - 1, 0, j)
            for i in range(m):
                top = self._minimumArea(grid, 0, i, j + 1, n - 1)
                bottom = self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1)
                # Only consider if all three rectangles have positive area
                if left > 0 and top > 0 and bottom > 0:
                    ans = min(ans, left + top + bottom)

        # Case 4: Right vertical rectangle, left split into top and bottom horizontal rectangles
        for j in range(n):
            right = self._minimumArea(grid, 0, m - 1, j, n - 1)
            for i in range(m):
                top = self._minimumArea(grid, 0, i, 0, j - 1)
                bottom = self._minimumArea(grid, i + 1, m - 1, 0, j - 1)
                # Only consider if all three rectangles have positive area
                if right > 0 and top > 0 and bottom > 0:
                    ans = min(ans, right + top + bottom)

        # Case 5: Three horizontal rectangles stacked
        for i1 in range(m):
            for i2 in range(i1 + 1, m):
                top = self._minimumArea(grid, 0, i1, 0, n - 1)
                middle = self._minimumArea(grid, i1 + 1, i2, 0, n - 1)
                bottom = self._minimumArea(grid, i2 + 1, m - 1, 0, n - 1)
                # Only consider if all three rectangles have positive area
                if top > 0 and middle > 0 and bottom > 0:
                    ans = min(ans, top + middle + bottom)

        # Case 6: Three vertical rectangles side by side
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                left = self._minimumArea(grid, 0, m - 1, 0, j1)
                middle = self._minimumArea(grid, 0, m - 1, j1 + 1, j2)
                right = self._minimumArea(grid, 0, m - 1, j2 + 1, n - 1)
                # Only consider if all three rectangles have positive area
                if left > 0 and middle > 0 and right > 0:
                    ans = min(ans, left + middle + right)

        return ans

    def _minimumArea(
        self,
        grid: list[list[int]],
        si: int,
        ei: int,
        sj: int,
        ej: int,
    ) -> int:
        # Initialize bounds for the bounding rectangle
        x1 = math.inf
        y1 = math.inf
        x2 = 0
        y2 = 0
        # Iterate over the subgrid to find min and max rows and columns with 1's
        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                if grid[i][j] == 1:
                    # Update min row
                    x1 = min(x1, i)
                    # Update min column
                    y1 = min(y1, j)
                    # Update max row
                    x2 = max(x2, i)
                    # Update max column
                    y2 = max(y2, j)
        # If no 1's found, return 0; else compute area
        return 0 if x1 == math.inf else (x2 - x1 + 1) * (y2 - y1 + 1)

    minimumSum = minimum_sum
