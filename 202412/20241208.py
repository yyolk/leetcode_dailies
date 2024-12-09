# https://leetcode.com/problems/two-best-non-overlapping-events/


class Solution:
    """2054. Two Best Non-Overlapping Events

    You are given a **0-indexed** 2D integer array of `events` where `events[i] =
    [startTimei, endTimei, valuei]`. The `ith` event starts at `startTimei`and ends at
    `endTimei`, and if you attend this event, you will receive a value of `valuei`. You
    can choose **at most** **two** **non-overlapping** events to attend such that the
    sum of their values is **maximized**.

    Return *this **maximum** sum.*

    Note that the start time and end time is **inclusive**: that is, you cannot attend
    two events where one of them starts and the other ends at the same time. More
    specifically, if you attend an event with end time `t`, the next event must start at
    or after `t + 1`."""

    def max_two_events(self, events: list[list[int]]) -> int:
        # Initialize variables for tracking maximum values
        maximum_value_from_first_event = 0
        maximum_sum_of_two_events = 0

        # Unpack start times, end times, and values from events
        start_times, end_times, values = zip(*events)

        # Sort start times with their corresponding values for the second meeting
        start_times_for_second_meeting = sorted(zip(start_times, values))

        # Sort end times with their corresponding values for the first meeting
        end_times_for_first_meeting = iter(sorted(zip(end_times, values)))

        # Get the first event's end time and value from the sorted iterator
        end_time_of_first_event, value_of_first_event = next(
            end_times_for_first_meeting
        )

        # Iterate through potential start times for the second meeting
        for (
            start_time_of_second_event,
            value_of_second_event,
        ) in start_times_for_second_meeting:

            # Skip events where the first meeting's end time overlaps with the second's start time
            while end_time_of_first_event < start_time_of_second_event:
                # Update the maximum value that can be obtained from the first event
                maximum_value_from_first_event = max(
                    maximum_value_from_first_event, value_of_first_event
                )
                end_time_of_first_event, value_of_first_event = next(
                    end_times_for_first_meeting
                )

            # Check if combining the current maximum first event value with the second event's value provides a new maximum
            maximum_sum_of_two_events = max(
                maximum_sum_of_two_events,
                maximum_value_from_first_event + value_of_second_event,
            )

        # Return the maximum sum achievable with two non-overlapping events
        return maximum_sum_of_two_events

    maxTwoEvents = max_two_events
