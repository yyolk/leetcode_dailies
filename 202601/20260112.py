# https://leetcode.com/problems/minimum-time-visiting-all-points


class Solution:
    """1266. Minimum Time Visiting All Points

    On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
    Return the minimum time in seconds to visit all the points in the order given by
    points.

    You can move according to these rules:
    - In 1 second, you can either:
      - move vertically by one unit,
      - move horizontally by one unit, or
      - move diagonally (one unit vertically and one unit horizontally).

    You must visit the points in the given order. Passing through later points is
    allowed but does not count as a visit.
    """
    def min_time_to_visit_all_points(self, points: list[list[int]]) -> int:
        # Total time starts at 0 (we begin at the first point)
        total_time = 0
        
        # Pair consecutive points efficiently
        for prev, curr in zip(points[:-1], points[1:]):
            # Absolute differences in coordinates
            dx = abs(curr[0] - prev[0])
            dy = abs(curr[1] - prev[1])
            
            # Chebyshev distance: max(dx, dy) seconds needed
            # Diagonal moves reduce both dx and dy by 1 per second
            total_time += max(dx, dy)
        
        return total_time
    
    minTimeToVisitAllPoints = min_time_to_visit_all_points