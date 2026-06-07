# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/


class Solution:
    """3195. Find the Minimum Area to Cover All Ones I

    You are given a 2D **binary** array `grid`. Find a rectangle with horizontal and
    vertical sides with the **smallest** area, such that all the 1"s in `grid` lie
    inside this rectangle.

    Return the **minimum** possible area of the rectangle."""

    def minimum_area(self, grid: list[list[int]]) -> int:
        # Handle empty grid case
        if not grid or not grid[0]:
            return 0
        # Get dimensions
        m, n = len(grid), len(grid[0])
        # Initialize bounds for rows and columns containing 1"s
        min_r = float("inf")
        max_r = float("-inf")
        min_c = float("inf")
        max_c = float("-inf")
        # Flag to check if any 1 exists
        has_one = False
        # Iterate through each cell to find bounds of 1"s
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    has_one = True
                    # Update minimum row index
                    min_r = min(min_r, r)
                    # Update maximum row index
                    max_r = max(max_r, r)
                    # Update minimum column index
                    min_c = min(min_c, c)
                    # Update maximum column index
                    max_c = max(max_c, c)
        # If no 1"s found, area is 0
        if not has_one:
            return 0
        # Calculate height of bounding rectangle
        height = max_r - min_r + 1
        # Calculate width of bounding rectangle
        width = max_c - min_c + 1
        # Compute and return area
        return height * width

    minimumArea = minimum_area
