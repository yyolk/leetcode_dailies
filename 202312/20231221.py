# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/


class Solution:
    """1637. Widest Vertical Area Between Two Points Containing No Points

    Given `n` `points` on a 2D plane where `points[i] = [xi, yi]`, Return*the **widest
    vertical area** between two points such that no points are inside the area.*

    A **vertical area** is an area of fixed-width extending infinitely along the y-axis
    (i.e., infinite height). The **widest vertical area** is the one with the maximum
    width.

    Note that points **on the edge** of a vertical area **are not** considered included
    in the area.
    """

    def max_width_of_vertical_area(self, points: list[list[int]]) -> int:
        # Sort the points based on x-coordinates
        points.sort(key=lambda x: x[0])

        # Initialize the maximum width to zero
        max_width = 0

        # Iterate through the sorted points and calculate the width
        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)

        return max_width

    maxWidthOfVerticalArea = max_width_of_vertical_area
