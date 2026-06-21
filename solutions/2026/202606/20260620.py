# https://leetcode.com/problems/maximum-building-height/


class Solution:
    """1840. Maximum Building Height

    You want to build n new buildings in a city. The new buildings will be built in a
    line and are labeled from 1 to n. Heights non-negative ints, height[1] must be 0,
    adjacent differ by <=1. Given restrictions[i]=[idi, maxHeighti] (building idi <=
    maxHeighti). Return max possible height of tallest building.
    """

    def max_building(self, n: int, restrictions: list[list[int]]) -> int:
        # Sorted list reusing original sublists (no copy, saves alloc/time)
        points = sorted(restrictions + [[1, 0]])
        # Forward: tighten max heights propagating from left
        for i in range(1, len(points)):
            dist = points[i][0] - points[i - 1][0]
            points[i][1] = min(points[i][1], points[i - 1][1] + dist)
        # Backward: tighten propagating from right
        for i in range(len(points) - 2, -1, -1):
            dist = points[i + 1][0] - points[i][0]
            points[i][1] = min(points[i][1], points[i + 1][1] + dist)
        # Max of tightened heights at anchors
        ans = max(h for _, h in points)
        # Max achievable peak between each consecutive pair
        for i in range(len(points) - 1):
            lp, lh = points[i]
            rp, rh = points[i + 1]
            ans = max(ans, (lh + rh + rp - lp) // 2)
        # Ramp-up from last anchor to n (always safe, +0 if at n)
        ans = max(ans, points[-1][1] + n - points[-1][0])
        return ans

    maxBuilding = max_building
