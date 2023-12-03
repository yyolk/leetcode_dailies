# https://leetcode.com/problems/minimum-time-visiting-all-points/


class Solution:
    """1266. Minimum Time Visiting All Points

    On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`.
    Return *the **minimum time** in seconds to visit all the points in the order given
    by* `points`.

    You can move according to these rules:

    * In `1` second, you can either:

            + move vertically by one unit,

            + move horizontally by one unit, or

            + move diagonally `sqrt(2)` units (in other words, move one unit vertically
    then one unit horizontally in `1` second).

    * You have to visit the points in the same order as they appear in the array.

    * You are allowed to pass through points that appear later in the order, but these
    do not count as visits.
    """

    def min_time_to_visit_all_points(self, points: list[list[int]]) -> int:
        """Minimum time for visiting all points.

        Args:
            points: The input list of points of a 2D plane of coords like x, y to visit
                in sequence order.

        Returns:
            The minimum time in seconds to visit all the points in the order given.
        """
        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            # The minimum time to move from one point to another is the maximum of
            # dx and dy because you can move vertically, horizontally, or diagonally.
            min_time = max(dx, dy)

            total_time += min_time

        return total_time

    minTimeToVisitAllPoints = min_time_to_visit_all_points
