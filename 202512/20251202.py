# https://leetcode.com/problems/count-number-of-trapezoids-i
from collections import Counter


class Solution:
    """3623. Count Number of Trapezoids I

    You are given a 2D integer array points, where points[i] = [xi, yi]
    represents the coordinates of the ith point on the Cartesian plane.

    A horizontal trapezoid is a convex quadrilateral with at least one pair
    of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel
    if and only if they have the same slope.

    Return the number of unique horizontal trapezoids that can be formed by
    choosing any four distinct points from points.

    Since the answer may be very large, return it modulo 10^9 + 7.
    """
    def count_trapezoids(self, points: list[list[int]]) -> int:
        MOD = 10**9 + 7
        # Group points by y-coordinate using Counter
        freq = Counter(y for x, y in points)
        # Compute combinations C(n, 2) for each y-group
        combs = [cnt * (cnt - 1) // 2 for cnt in freq.values()]
        # Sum of all C(n, 2)
        sum_combs = sum(combs) % MOD
        # Sum of squares of C(n, 2)
        sum_sq = sum(c * c for c in combs) % MOD
        # (sum_combs^2 - sum_sq) / 2 mod MOD
        inv2 = pow(2, MOD - 2, MOD)
        total = ((sum_combs * sum_combs % MOD - sum_sq + MOD) % MOD * inv2) % MOD
        return total

    countTrapezoids = count_trapezoids