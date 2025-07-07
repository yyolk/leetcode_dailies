# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/


class Solution:
    """1353. Maximum Number of Events That Can Be Attended

    You are given an array of `events` where `events[i] = [startDayi, endDayi]`. Every
    event `i` starts at `startDayi`and ends at `endDayi`.

    You can attend an event `i` at any day `d` where `startTimei <= d <= endTimei`. You
    can only attend one event at any time `d`.

    Return *the maximum number of events you can attend*."""

    def max_events(self, events: list[list[int]]) -> int:
        # Sort events by start day to process them chronologically
        events.sort(key=lambda x: x[0])
        
        # Min-heap to store end days of ongoing events
        ongoing = []
        
        # Counter for the number of events attended
        attended = 0
        
        # Index to track the current event in the sorted list
        i = 0
        
        # Maximum possible day as per constraints (1 <= startDayi <= endDayi <= 10^5)
        MAX_DAY = 100000
        
        # Iterate through each day from 1 to MAX_DAY
        for day in range(1, MAX_DAY + 1):
            # Add all events that start on the current day to the heap
            while i < len(events) and events[i][0] == day:
                heapq.heappush(ongoing, events[i][1])
                i += 1
            
            # Remove events that have ended before the current day
            while ongoing and ongoing[0] < day:
                heapq.heappop(ongoing)
            
            # If there are ongoing events, attend the one with the earliest end day
            if ongoing:
                heapq.heappop(ongoing)
                attended += 1
        
        return attended

    maxEvents = max_events
