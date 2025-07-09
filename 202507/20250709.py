# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/


class Solution:
    """3439. Reschedule Meetings for Maximum Free Time I

    You are given an integer `event_time` denoting the duration of an event, where the
    event occurs from time `t = 0` to time `t = event_time`.

    You are also given two integer arrays `start_time` and `end_time`, each of length
    `n`. These represent the start and end time of `n` **non-overlapping** meetings,
    where the `ith` meeting occurs during the time `[start_time[i], end_time[i]]`.

    You can reschedule **at most** `k` meetings by moving their start time while
    maintaining the **same duration**, to **maximize** the **longest** *continuous
    period of free time* during the event.

    The **relative** order of all the meetings should stay the *same* and they should
    remain non-overlapping.

    Return the **maximum** amount of free time possible after rearranging the meetings.

    **Note** that the meetings can **not** be rescheduled to a time outside the event.
    """

    def max_free_time(
        self, event_time: int, k: int, start_time: list[int], end_time: list[int]
    ) -> int: ...

    maxFreeTime = max_free_time
