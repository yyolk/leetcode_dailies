# https://leetcode.com/problems/count-number-of-trapezoids-ii/
from collections import defaultdict
from math import gcd


class Solution:
    """3625. Count Number of Trapezoids II

    You are given a 2D integer array points where points[i] = [xi, yi]
    represents the coordinates of the ith point on the Cartesian plane.

    Return the number of unique trapezoids that can be formed by choosing
    any four distinct points from points.

    A trapezoid is a convex quadrilateral with at least one pair of parallel
    sides. Two lines are parallel if and only if they have the same slope.
    """
    def count_trapezoids(self, points: List[List[int]]) -> int:
        # Group diagonals by midpoint and their normalized slope to count non-degenerate parallelograms
        mid_slope_count = defaultdict(lambda: defaultdict(int))
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                sx = points[i][0] + points[j][0]
                sy = points[i][1] + points[j][1]
                # Normalize slope for this diagonal
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(abs(dx), abs(dy))
                if g > 0:
                    dx //= g
                    dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                diag_slope = (dx, dy)
                mid_slope_count[(sx, sy)][diag_slope] += 1
        num_parall = 0
        for slope_dict in mid_slope_count.values():
            k = sum(slope_dict.values())
            if k < 2:
                continue
            total_ways = k * (k - 1) // 2
            degen = sum(m * (m - 1) // 2 for m in slope_dict.values())
            num_parall += total_ways - degen

        # Group segments by normalized slope and line intercept b
        seg_groups = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(abs(dx), abs(dy))
                if g > 0:
                    dx //= g
                    dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dx, dy)
                # Intercept b for line equation dx*y - dy*x = b
                b = dx * y1 - dy * x1
                seg_groups[slope][b] += 1

        # For each slope, count pairs of segments on different parallel lines
        total_incidences = 0
        for slope, b_dict in seg_groups.items():
            S = sum(b_dict.values())  # Total segments with this slope
            Q = sum(c * c for c in b_dict.values())
            num_for_slope = (S * S - Q) // 2
            total_incidences += num_for_slope

        # Trapezoids = incidences (counts each twice for parallelograms) - parallelograms
        return total_incidences - num_parall

    countTrapezoids = count_trapezoids