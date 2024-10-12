# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
from heapq import heappush, heappop


class Solution:
    """2406. Divide Intervals Into Minimum Number of Groups

    You are given a 2D integer array `intervals` where `intervals[i] = [lefti, righti]`
    represents the **inclusive** interval `[lefti, righti]`.

    You have to divide the intervals into one or more **groups** such that each interval
    is in **exactly** one group, and no two intervals that are in the same group
    **intersect** each other.

    Return *the **minimum** number of groups you need to make*.

    Two intervals **intersect** if there is at least one common number between them. For
    example, the intervals `[1, 5]` and `[5, 8]` intersect.

    """

    def min_groups(self, intervals: list[list[int]]) -> int:
        # Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        # Use a min heap to keep track of the end times of the groups
        heap = []
        for start, end in intervals:
            if heap and heap[0] < start:
                # If the smallest end time in the heap is before the start of the current interval,
                # we can use the same group, so remove that end time from heap
                heappop(heap)
            
            # Add the current interval's end time to the heap
            heappush(heap, end)
        
        # The size of the heap at the end represents the number of groups needed
        return len(heap)

    minGroups = min_groups
