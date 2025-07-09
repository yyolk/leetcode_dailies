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
    ) -> int:
        n = len(start_time)
        
        # Step 1: Compute the gaps (free time periods)
        # gap[i] represents the free time before meeting i (for i=0, from event start)
        # gap[n] is the free time after the last meeting
        gap = [start_time[0]]  # Free time from 0 to first meeting
        for i in range(1, n):
            gap.append(start_time[i] - end_time[i-1])  # Free time between meetings
        gap.append(event_time - end_time[n-1])  # Free time after last meeting
        
        # Step 2: Find maximum sum of k+1 consecutive gaps using sliding window
        # This represents the largest free time achievable by shifting k meetings
        window_size = k + 1
        current_sum = sum(gap[:window_size])  # Sum of first k+1 gaps
        max_free = current_sum
        
        # Slide the window over all possible sets of k+1 consecutive gaps
        for i in range(1, n - k + 1):
            # Remove the leftmost gap and add the next gap on the right
            current_sum = current_sum - gap[i-1] + gap[i + k]
            max_free = max(max_free, current_sum)
        
        # Return the maximum free time found
        return max_free

    maxFreeTime = max_free_time
