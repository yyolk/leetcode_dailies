# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/


class Solution:
    """1353. Maximum Number of Events That Can Be Attended

    You are given an array of `events` where `events[i] = [startDayi, endDayi]`. Every
    event `i` starts at `startDayi`and ends at `endDayi`.

    You can attend an event `i` at any day `d` where `startTimei <= d <= endTimei`. You
    can only attend one event at any time `d`.

    Return *the maximum number of events you can attend*."""

    def max_events(self, events: list[list[int]]) -> int: ...

    maxEvents = max_events
