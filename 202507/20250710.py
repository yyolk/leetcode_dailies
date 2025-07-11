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
    ) -> int:
        # Store the total number of meetings
        number_of_meetings = len(start_time)

        # Compute all gaps: start of event to first meeting, between meetings, and last meeting to end of event
        free_time_gaps = (
            [start_time[0]]
            + [start_time[i] - end_time[i - 1] for i in range(1, number_of_meetings)]
            + [event_time - end_time[-1]]
        )

        # Calculate the duration of each meeting
        meeting_durations = [
            end_time[i] - start_time[i] for i in range(number_of_meetings)
        ]

        # Determine the largest gap before any rescheduling
        initial_maximum_gap = max(free_time_gaps)

        # Initialize variables to track the three largest distinct gap sizes
        largest_gap_size = second_largest_gap_size = third_largest_gap_size = -1

        # Initialize counters for how many times each of the largest gap sizes appears
        largest_gap_count = second_largest_gap_count = third_largest_gap_count = 0

        # Iterate through all gaps to identify the top three largest gap sizes and their frequencies
        for current_gap in free_time_gaps:
            # Check if the current gap is larger than the largest recorded gap
            if current_gap > largest_gap_size:
                # Shift the third largest to second largest
                third_largest_gap_size, third_largest_gap_count = (
                    second_largest_gap_size,
                    second_largest_gap_count,
                )
                # Shift the second largest to largest
                second_largest_gap_size, second_largest_gap_count = (
                    largest_gap_size,
                    largest_gap_count,
                )
                # Set the new largest gap and reset its count to 1
                largest_gap_size, largest_gap_count = current_gap, 1
            # Check if the current gap equals the largest gap
            elif current_gap == largest_gap_size:
                # Increment the count of the largest gap
                largest_gap_count += 1
            # Check if the current gap is larger than the second largest gap
            elif current_gap > second_largest_gap_size:
                # Shift the third largest to second largest
                third_largest_gap_size, third_largest_gap_count = (
                    second_largest_gap_size,
                    second_largest_gap_count,
                )
                # Set the new second largest gap and reset its count to 1
                second_largest_gap_size, second_largest_gap_count = current_gap, 1
            # Check if the current gap equals the second largest gap
            elif current_gap == second_largest_gap_size:
                # Increment the count of the second largest gap
                second_largest_gap_count += 1
            # Check if the current gap is larger than the third largest gap
            elif current_gap > third_largest_gap_size:
                # Set the new third largest gap and reset its count to 1
                third_largest_gap_size, third_largest_gap_count = current_gap, 1
            # Check if the current gap equals the third largest gap
            elif current_gap == third_largest_gap_size:
                # Increment the count of the third largest gap
                third_largest_gap_count += 1

        # Initialize the result with the initial maximum gap
        maximum_free_time = initial_maximum_gap

        # Iterate over each meeting to try rescheduling it
        for meeting_index in range(number_of_meetings):
            # Get the gap before the current meeting
            gap_before_meeting = free_time_gaps[meeting_index]
            # Get the gap after the current meeting
            gap_after_meeting = free_time_gaps[meeting_index + 1]

            # Count how many of the largest gaps are involved (gap before or after)
            largest_gaps_involved = (gap_before_meeting == largest_gap_size) + (
                gap_after_meeting == largest_gap_size
            )

            # Determine the largest gap not involved in this rescheduling
            if largest_gaps_involved < largest_gap_count:
                # If not all largest gaps are involved, use the largest gap size
                maximum_other_gap = largest_gap_size
            else:
                # Count how many of the second largest gaps are involved
                second_largest_gaps_involved = (
                    gap_before_meeting == second_largest_gap_size
                ) + (gap_after_meeting == second_largest_gap_size)
                # Check if not all second largest gaps are involved
                if second_largest_gaps_involved < second_largest_gap_count:
                    # Use the second largest gap size
                    maximum_other_gap = second_largest_gap_size
                else:
                    # Fall back to the third largest gap size
                    maximum_other_gap = third_largest_gap_size

            # Calculate the merged gap if the current meeting is removed
            merged_gap_size = (
                gap_before_meeting
                + meeting_durations[meeting_index]
                + gap_after_meeting
            )

            # Check if there is another gap large enough to fit the meeting
            if maximum_other_gap >= meeting_durations[meeting_index]:
                # If yes, take the maximum of the merged gap and the other gap
                free_time_for_this_reschedule = (
                    merged_gap_size
                    if merged_gap_size > maximum_other_gap
                    else maximum_other_gap
                )
            else:
                # If no, the free time is the merged gap minus the meeting duration
                free_time_for_this_reschedule = (
                    merged_gap_size - meeting_durations[meeting_index]
                )

            # Update the maximum free time if this rescheduling yields a better result
            if free_time_for_this_reschedule > maximum_free_time:
                maximum_free_time = free_time_for_this_reschedule

        # Return the maximum free time achievable after considering all reschedulings
        return maximum_free_time

    maxFreeTime = max_free_time
