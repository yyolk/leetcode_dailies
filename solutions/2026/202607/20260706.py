# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    """1288. Remove Covered Intervals

    Given an array intervals where intervals[i] = [li, ri] represent the interval
    [li, ri), remove all intervals that are covered by another interval in the list.
    The interval [a, b) is covered by the interval [c, d) if and only if c <= a and
    b <= d.
    Return the number of remaining intervals.
    Constraints:
    * 1 <= intervals.length <= 1000
    * intervals[i].length == 2
    * 0 <= li < ri <= 105
    * All the given intervals are unique."""

    def remove_covered_intervals(self, intervals: list[list[int]]) -> int:
        # Sort: start asc, then end desc (longer first on tie; ensures prior can cover)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remaining = 0
        max_end = -1
        for start, end in intervals:
            # Not covered only if extends max_end (all priors have <=start)
            if end > max_end:
                remaining += 1
                max_end = end  # new farthest reach
        return remaining

    removeCoveredIntervals = remove_covered_intervals
