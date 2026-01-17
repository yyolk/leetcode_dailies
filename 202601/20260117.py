# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles


class Solution:
    """3047. Find the Largest Area of Square Inside Two Rectangles

    There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given
    two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and
    topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith
    rectangle, respectively.

    You need to find the maximum area of a square that can fit inside the intersecting region of
    at least two rectangles. Return 0 if such a square does not exist.
    """
    def largest_square_area(self, bottom_left: list[list[int]], top_right: list[list[int]]) -> int:
        n = len(bottom_left)
        max_side = 0

        # Check every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Compute intersection boundaries
                left = max(bottom_left[i][0], bottom_left[j][0])
                right = min(top_right[i][0], top_right[j][0])
                bottom = max(bottom_left[i][1], bottom_left[j][1])
                top = min(top_right[i][1], top_right[j][1])

                # If no intersection (or degenerate), skip
                if left >= right or bottom >= top:
                    continue

                # The largest square that fits in this intersection
                # is limited by the smaller of width and height
                side = min(right - left, top - bottom)
                max_side = max(max_side, side)

        # Area = side²
        return max_side * max_side

    largestSquareArea = largest_square_area