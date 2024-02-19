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
    **including** `a` and **not including** `b`.

    """

    def most_booked(self, n: int, meetings: list[list[int]]) -> int:
        # Initialize arrays to keep track of the number of meetings and end times for each room
        ans = [0] * n
        times = [0] * n

        # Sort meetings based on their start times
        meetings.sort()

        # Iterate through the sorted meetings
        for start, end in meetings:
            flag = False
            minind = -1
            val = float("inf")

            # Check each room to find the earliest available room
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    # Room is available, update its information
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break

            if not flag:
                # No available room, schedule the meeting in the room with the earliest end time
                ans[minind] += 1
                times[minind] += end - start

        # Find the room with the most meetings
        maxi = -1
        id_ = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id_ = i

        # Return the room number that held the most meetings
        return id_

    mostBooked = most_booked
