# https://leetcode.com/problems/largest-triangle-area/


class Solution:
    """812. Largest Triangle Area

    Given an array of points on the **X-Y** plane `points` where `points[i] = [xi, yi]`,
    return *the area of the largest triangle that can be formed by any three different
    points*. Answers within `10-5` of the actual answer will be accepted."""

    def largest_triangle_area(self, points: list[list[int]]) -> float:
        # Initialize maximum area to 0
        max_area = 0.0
        n = len(points)
        # Iterate over all possible combinations of three points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    # Compute area using the shoelace formula: (1/2) * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    # Update max_area if current area is larger
                    if area > max_area:
                        max_area = area
        return max_area

    largestTriangleArea = largest_triangle_area
