# https://leetcode.com/problems/rectangle-overlap/


class Solution:
    """836. Rectangle Overlap

    An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where
    `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the
    coordinate of its top-right corner. Its top and bottom edges are parallel to
    the X-axis, and its left and right edges are parallel to the Y-axis.

    Two rectangles overlap if the area of their intersection is **positive**. To
    be clear, two rectangles that only touch at the corner or edges do not
    overlap.

    Given two axis-aligned rectangles `rec1` and `rec2`, return `true` *if they
    overlap, otherwise return* `false`.

    Constraints:

    * `rec1.length == 4`

    * `rec2.length == 4`

    * `-109 <= rec1[i], rec2[i] <= 109`

    * `rec1` and `rec2` represent a valid rectangle with a non-zero area.
    """

    def is_rectangle_overlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Strict inequalities: shared edges/corners have zero area, so no overlap.
        return (
            rec1[0] < rec2[2]
            and rec2[0] < rec1[2]
            and rec1[1] < rec2[3]
            and rec2[1] < rec1[3]
        )

    isRectangleOverlap = is_rectangle_overlap
