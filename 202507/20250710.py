# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/


class Solution:
    """3440. Reschedule Meetings for Maximum Free Time II

    You are given an integer `event_time` denoting the duration of an event. You are
    also given two integer arrays `start_time` and `end_time`, each of length `n`.

    These represent the start and end times of `n` **non-overlapping** meetings that
    occur during the event between time `t = 0` and time `t = event_time`, where the
    `ith` meeting occurs during the time `[start_time[i], end_time[i]].`

    You can reschedule **at most** one meeting by moving its start time while
    maintaining the **same duration**, such that the meetings remain non-overlapping, to
    **maximize** the **longest** *continuous period of free time* during the event.

    Return the **maximum** amount of free time possible after rearranging the meetings.

    **Note** that the meetings can **not** be rescheduled to a time outside the event
    and they should remain non-overlapping.

    **Note:** *In this version*, it is **valid** for the relative ordering of the
    meetings to change after rescheduling one meeting."""

    def max_free_time(
        self, event_time: int, start_time: list[int], end_time: list[int]
    ) -> int: ...

    maxFreeTime = max_free_time
