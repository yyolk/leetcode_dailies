# https://leetcode.com/problems/count-covered-buildings/
from collections import defaultdict


class Solution:
    """3531. Count Covered Buildings

    You are given a positive integer n, representing an n x n city. You are
    also given a 2D grid buildings, where buildings[i] = [x, y] denotes a
    unique building located at coordinates [x, y].

    A building is covered if there is at least one building in all four
    directions: left, right, above, and below.

    Return the number of covered buildings.
    """
    def count_covered_buildings(self, n: int, buildings: list[list[int]]) -> int:
        # Handle empty case
        if not buildings:
            return 0

        # Track min/max x per row (y) for left/right checks
        row_min_x = defaultdict(lambda: float('inf'))
        row_max_x = defaultdict(lambda: -float('inf'))
        # Track min/max y per column (x) for above/below checks
        col_min_y = defaultdict(lambda: float('inf'))
        col_max_y = defaultdict(lambda: -float('inf'))

        # Populate min/max values
        for x, y in buildings:
            row_min_x[y] = min(row_min_x[y], x)
            row_max_x[y] = max(row_max_x[y], x)
            col_min_y[x] = min(col_min_y[x], y)
            col_max_y[x] = max(col_max_y[x], y)

        # Count buildings strictly between min/max in row and column
        count = 0
        for x, y in buildings:
            # Check left/right (row) and above/below (column)
            if (row_min_x[y] < x < row_max_x[y] and
                col_min_y[x] < y < col_max_y[x]):
                count += 1

        return count

    countCoveredBuildings = count_covered_buildings