# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

from collections import deque

class Solution:
    """3464. Maximize the Distance Between Points on a Square

    You are given an integer side, representing the edge length of a square with
    corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian
    plane. You are also given a positive integer k and a 2D integer array
    points, where points[i] = [xi, yi] represents the coordinate of a point
    lying on the boundary of the square. You need to select k elements among
    points such that the minimum Manhattan distance between any two points is
    maximized. Return the maximum possible minimum Manhattan distance between
    the selected k points. The Manhattan Distance between two cells (xi, yi) and
    (xj, yj) is |xi - xj| + |yi - yj|.
    """
    def max_distance(self, side: int, points: list[list[int]], k: int) -> int:
        # Group and sort points clockwise along perimeter (ensures consecutive
        # selected points determine min Manhattan due to square geometry)
        left = sorted(p for p in points if p[0] == 0 and p[1] > 0)
        top = sorted(p for p in points if p[1] == side and p[0] > 0)
        right = sorted((p for p in points if p[0] == side and p[1] < side),
                       reverse=True)
        bottom = sorted((p for p in points if p[1] == 0), reverse=True)
        ordered = left + top + right + bottom

        def is_valid(m: int) -> bool:
            if not ordered:
                return k <= 0
            # deque stores (start_x, start_y, end_x, end_y, chain_length) for
            # O(1) amortized extension of valid chains
            dq = deque([(ordered[0][0], ordered[0][1],
                         ordered[0][0], ordered[0][1], 1)])
            max_len = 1
            for px, py in ordered[1:]:
                # Start new chain at current point
                sx, sy = px, py
                length = 1
                # Slide window: drop prefixes whose end is too close; extend
                # from farthest valid start if full dist also >= m
                while dq and abs(px - dq[0][2]) + abs(py - dq[0][3]) >= m:
                    if (abs(px - dq[0][0]) + abs(py - dq[0][1]) >= m and
                        dq[0][4] + 1 >= length):
                        sx, sy = dq[0][0], dq[0][1]
                        length = dq[0][4] + 1
                        max_len = max(max_len, length)
                    dq.popleft()
                dq.append((sx, sy, px, py, length))
            return max_len >= k

        # Binary search on answer (max min dist <= side by geometry)
        lo = 0
        hi = side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_valid(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    maxDistance = max_distance