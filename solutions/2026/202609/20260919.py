# https://leetcode.com/problems/circle-and-rectangle-overlapping/


class Solution:
    """1401. Circle and Rectangle Overlapping

    You are given a circle represented as `(radius, x_center, y_center)` and an
    axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)`
    are the coordinates of the bottom-left corner, and `(x2, y2)` are the
    coordinates of the top-right corner of the rectangle.

    Return `true` if the circle and rectangle are overlapped otherwise return
    `false`. In other words, check if there is any point `(xi, yi)` that belongs
    to the circle and the rectangle at the same time.

    Constraints:

    * `1 <= radius <= 2000`
    * `-104 <= x_center, y_center <= 104`
    * `-104 <= x1 < x2 <= 104`
    * `-104 <= y1 < y2 <= 104`
    """

    def check_overlap(
        self,
        radius: int,
        x_center: int,
        y_center: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        """True if any point lies in both the circle and the rectangle."""
        # Clamp the center onto the rectangle; leftover is the nearest gap.
        nearest_x = min(max(x_center, x1), x2)
        nearest_y = min(max(y_center, y1), y2)
        dx = x_center - nearest_x
        dy = y_center - nearest_y
        return dx * dx + dy * dy <= radius * radius

    checkOverlap = check_overlap
