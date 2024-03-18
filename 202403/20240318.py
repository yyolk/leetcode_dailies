# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    """452. Minimum Number of Arrows to Burst Balloons

    There are some spherical balloons taped onto a flat wall that represents the XY-
    plane. The balloons are represented as a 2D integer array `points` where `points[i]
    = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between
    `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

    Arrows can be shot up **directly vertically** (in the positive y-direction) from
    different points along the x-axis. A balloon with `xstart` and `xend` is **burst**
    by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the
    number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
    bursting any balloons in its path.

    Given the array `points`, return *the **minimum** number of arrows that must be shot
    to burst all balloons*.

    """

    def find_min_arrow_shots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        
        # Sort the points by their x-coordinates
        points.sort(key=lambda x: x[0])
        
        # Initialize the minimum number of arrows
        min_arrows = 1
        
        # Keep track of the current end point
        current_end = points[0][1]
        
        # Iterate over the remaining points
        for i in range(1, len(points)):
            start, end = points[i]
            
            # If the current balloon's start point is greater than the previous end point, we need an additional arrow
            if start > current_end:
                min_arrows += 1
                current_end = end
            
            # Update the current end point if necessary
            elif end > current_end:
                current_end = end
        
        return min_arrows

    findMinArrowShots = find_min_arrow_shots
