# https://leetcode.com/problems/meeting-rooms-iii
import heapq


class Solution:
    """
    2402. Meeting Rooms III

    Given n rooms and a list of meetings [start, end], assign each meeting to the
    lowest-numbered available room. If no room is free, delay the meeting until one
    becomes available, preserving duration. Prioritize meetings by original start
    time when rooms free up. Return the room number that hosted the most meetings
    (lowest number if tie).
    """

    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time for processing in order
        meetings.sort()
        
        # Min-heap: (next_free_time, room_id) - tracks when each room is free
        available = list(range(n))
        heapq.heapify(available)
        
        # Min-heap: (end_time, room_id) - tracks ongoing meetings
        busy = []
        
        # Count meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free up all rooms that finish by current meeting's start time
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            # Determine actual start time for this meeting
            if available:
                # Room available now - use lowest numbered
                room = heapq.heappop(available)
                actual_start = start
            else:
                # No room free - wait for earliest finishing room
                finish_time, room = heapq.heappop(busy)
                actual_start = finish_time
            
            # Schedule meeting end and increment usage count
            actual_end = actual_start + duration
            heapq.heappush(busy, (actual_end, room))
            count[room] += 1
        
        # Find room with max meetings, break ties by lowest room number
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
        
        return -1  # Unreachable