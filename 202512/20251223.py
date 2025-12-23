# https://leetcode.com/problems/two-best-non-overlapping-events


class Solution:
    """2054. Two Best Non-Overlapping Events

    You are given a 0-indexed 2D integer array of events where events[i] =
    [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends
    at endTimei, and if you attend this event, you will receive a value of
    valuei. You can choose at most two non-overlapping events to attend such
    that the sum of their values is maximized.

    Return this maximum sum.

    Note that the start time and end time is inclusive: that is, you cannot
    attend two events where one of them starts and the other ends at the same
    time. More specifically, if you attend an event with end time t, the next
    event must start at or after t + 1.
    """
    def max_two_events(self, events: list[list[int]]) -> int:
        from typing import List
        
        n = len(events)
        if n == 0:
            return 0
        
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        
        # suffixMax[i] = max value of any event from i to n-1
        suffix_max = [0] * n
        suffix_max[n-1] = events[n-1][2]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i+1])
        
        ans = 0
        # Consider each event i as the first (earlier) one
        for i in range(n):
            # Update with single event value
            ans = max(ans, events[i][2])
            
            # Binary search for the leftmost event j > i with start_j > end_i
            left, right = i + 1, n - 1
            next_idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:  # strict > handles t+1 rule
                    next_idx = mid
                    right = mid - 1               # try to find earlier valid
                else:
                    left = mid + 1
            
            # If a non-overlapping later event exists, add its suffix max
            if next_idx != -1:
                ans = max(ans, events[i][2] + suffix_max[next_idx])
        
        return ans

    maxTwoEvents = max_two_events