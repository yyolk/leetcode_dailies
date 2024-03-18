# https://leetcode.com/problems/insert-interval/


class Solution:
    """57. Insert Interval

    You are given an array of non-overlapping intervals `intervals` where `intervals[i]
    = [starti, endi]` represent the start and the end of the `ith` interval and
    `intervals` is sorted in ascending order by `starti`. You are also given an interval
    `new_interval = [start, end]` that represents the start and end of another interval.

    Insert `new_interval` into `intervals` such that `intervals` is still sorted in
    ascending order by `starti` and `intervals` still does not have any overlapping
    intervals (merge overlapping intervals if necessary).

    Return `intervals` *after the insertion*.

    **Note** that you don't need to modify `intervals` in-place. You can make a new
    array and return it.

    """

    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        merged = []
        i = 0

        # Add intervals that come before the new interval
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge intervals that overlap with the new interval
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval = [
                min(new_interval[0], intervals[i][0]),
                max(new_interval[1], intervals[i][1]),
            ]
            i += 1
        merged.append(new_interval)

        # Add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
