# https://leetcode.com/problems/meeting-rooms-iii/
import heapq


class Solution:
    """2402. Meeting Rooms III

    You are given an integer `n`. There are `n` rooms numbered from `0` to `n - 1`.

    You are given a 2D integer array `meetings` where `meetings[i] = [starti, endi]`
    means that a meeting will be held during the **half-closed** time interval `[starti,
    endi)`. All the values of `starti` are **unique**.

    Meetings are allocated to rooms in the following manner:

    1. Each meeting will take place in the unused room with the **lowest** number.

    2. If there are no available rooms, the meeting will be delayed until a room becomes
    free. The delayed meeting should have the **same** duration as the original meeting.

    3. When a room becomes unused, meetings that have an earlier original **start** time
    should be given the room.

    Return *the **number** of the room that held the most meetings.* If there are
    multiple rooms, return *the room with the **lowest** number.*

    A **half-closed interval** `[a, b)` is the interval between `a` and `b`
    **including** `a` and **not including** `b`."""

    def most_booked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        # Initialize count of meetings per room
        counts = [0] * n
        # Min-heap for available rooms
        available = list(range(n))
        heapq.heapify(available)
        # Min-heap for busy rooms: (end_time, room)
        busy = []
        
        for start, end in meetings:
            duration = end - start
            # Free up rooms that are done by current start time
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                # Assign the lowest available room
                room = heapq.heappop(available)
                counts[room] += 1
                new_end = start + duration
                heapq.heappush(busy, (new_end, room))
            else:
                if busy:
                    # Delay meeting until the earliest busy room frees up
                    free_time, room = heapq.heappop(busy)
                    counts[room] += 1
                    new_end = free_time + duration
                    heapq.heappush(busy, (new_end, room))
        
        # Find the maximum meetings count
        max_count = max(counts)
        # Return the lowest room number with max meetings
        for i in range(n):
            if counts[i] == max_count:
                return i
        return -1  # Should not reach here

    mostBooked = most_booked
