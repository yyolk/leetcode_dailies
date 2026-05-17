# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
from math import inf


class Solution:
    """3025. Find the Number of Ways to Place People I

    You are given a 2D array `points` of size `n x 2` representing integer coordinates
    of some points on a 2D plane, where `points[i] = [xi, yi]`.

    Count the number of pairs of points `(A, B)`, where

    * `A` is on the **upper left** side of `B`, and

    * there are no other points in the rectangle (or line) they make (**including the
    border**).

    Return the count."""

    def number_of_pairs(self, points: list[list[int]]) -> int:
        # Sort points by x ascending, then by y descending for same x
        points.sort(key=lambda p: (p[0], -p[1]))

        # Initialize count of valid pairs
        ans = 0

        # Iterate over each possible Chisato position (upper left)
        for i, (_, y1) in enumerate(points):
            # Initialize the maximum y seen for accepted Takina positions
            max_y = -inf

            # Check each potential Takina position after i
            for _, y2 in points[i + 1 :]:
                # If y2 is between max_y (exclusive) and y1 (inclusive),
                # it forms a valid pair without enclosing prior points
                if max_y < y2 <= y1:
                    # Update the max y to current y2
                    max_y = y2
                    # Increment the pair count
                    ans += 1

        # Return the total number of valid pairs
        return ans

    numberOfPairs = number_of_pairs
