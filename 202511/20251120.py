# https://leetcode.com/problems/set-intersection-size-at-least-two/
import bisect


class Solution:
    """757. Set Intersection Size At Least Two

    You are given a 2D integer array intervals where intervals[i] =
    [starti, endi] represents all the integers from starti to endi
    inclusively.

    A containing set is an array nums where each interval from intervals
    has at least two integers in nums.

    For example, if intervals = [[1,3], [3,7], [8,9]], then
    [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.

    Return the minimum possible size of a containing set.
    """
    def intersection_size_two(self, intervals: list[list[int]]) -> int:
        # Sort intervals by their end points in ascending order
        intervals.sort(key=lambda x: x[1])
        # Sorted list to maintain placed points for range queries
        points = []
        # Set for O(1) existence checks
        taken = set()
        for interval in intervals:
            start, end = interval
            # Find indices for points in [start, end]
            left = bisect.bisect_left(points, start)
            right = bisect.bisect_right(points, end)
            # Count existing points in the interval
            k = right - left
            # Calculate how many points to add (0, 1, or 2)
            to_add = 2 - k
            if to_add <= 0:
                continue
            # Start from the rightmost position to place new points
            pos = end
            added = 0
            while added < to_add and pos >= start:
                # Skip if position already taken
                if pos not in taken:
                    # Insert into sorted list
                    bisect.insort(points, pos)
                    # Add to set
                    taken.add(pos)
                    added += 1
                # Move to next lower position
                pos -= 1
        # The size is the number of unique points
        return len(points)

    intersectionSizeTwo = intersection_size_two