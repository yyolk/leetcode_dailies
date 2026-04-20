
class Solution:
    """2078. Two Furthest Houses With Different Colors
    
    There are n houses evenly lined up on the street, and each house is
    beautifully painted. You are given a 0-indexed integer array colors of
    length n, where colors[i] represents the color of the i^th house.
    Return the maximum distance between two houses with different colors.
    The distance between the i^th and j^th houses is abs(i - j), where abs(x)
    is the absolute value of x.
    """
    def max_distance(self, colors: list[int]) -> int:
        n: int = len(colors)
        max_d: int = 0
        for i in range(n):
            # update max distance from left end to any house differing in color
            if colors[i] != colors[0]:
                max_d = max(max_d, i)
            # update max distance from right end to any house differing in color
            if colors[i] != colors[-1]:
                max_d = max(max_d, n - 1 - i)
        return max_d

    maxDistance = max_distance