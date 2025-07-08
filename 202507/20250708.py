# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/


class Solution:
    """1751. Maximum Number of Events That Can Be Attended II

    You are given an array of `events` where `events[i] = [startDayi, endDayi, valuei]`.
    The `ith` event starts at `startDayi`and ends at `endDayi`, and if you attend this
    event, you will receive a value of `valuei`. You are also given an integer `k` which
    represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event, you must
    attend the **entire** event. Note that the end day is **inclusive**: that is, you
    cannot attend two events where one of them starts and the other ends on the same
    day.

    Return *the **maximum sum** of values that you can receive by attending events.*"""

    def max_value(self, events: list[list[int]], max_events_allowed: int) -> int:
        # Sort events by start day to process them chronologically
        events.sort(key=lambda event: event[0])
        
        # Extract start days into a list for binary search
        event_start_days = [event[0] for event in events]
        
        # Store the total number of events
        total_events = len(events)
        
        # Initialize array to store indices of next non-overlapping events
        next_non_overlapping_indices = [0] * total_events
        
        # Compute the index of the next non-overlapping event for each event
        for current_index in range(total_events):
            # Get the end day of the current event
            current_event_end_day = events[current_index][1]
            # Use binary search to find the first event that starts after the current event ends
            next_non_overlapping_indices[current_index] = bisect.bisect_right(event_start_days, current_event_end_day)
        
        # Initialize array to store maximum values for the previous iteration
        previous_max_values = [0] * (total_events + 1)
        
        # Compute maximum value achievable by attending one event, processing events in reverse
        for current_index in range(total_events - 1, -1, -1):
            # Update maximum value by comparing with the next index and current event's value
            previous_max_values[current_index] = max(previous_max_values[current_index + 1], events[current_index][2])
        
        # Initialize result with the maximum value for one event
        maximum_total_value = previous_max_values[0]
        
        # Iterate for each allowed event count from 2 to max_events_allowed
        for current_event_count in range(2, max_events_allowed + 1):
            # Initialize array for current iteration's maximum values
            current_max_values = [0] * (total_events + 1)
            
            # Process events in reverse order to compute maximum values
            for current_index in range(total_events - 1, -1, -1):
                # Calculate value if we attend the current event
                value_if_attend = events[current_index][2]
                
                # Get the index of the next non-overlapping event
                next_event_index = next_non_overlapping_indices[current_index]
                
                # If a non-overlapping event exists, add its maximum value
                if next_event_index <= total_events:
                    value_if_attend += previous_max_values[next_event_index]
                
                # Update current maximum by choosing between attending or skipping the event
                current_max_values[current_index] = max(current_max_values[current_index + 1], value_if_attend)
            
            # Update overall maximum with the result of current iteration
            maximum_total_value = max(maximum_total_value, current_max_values[0])
            
            # Update previous_max_values for the next iteration
            previous_max_values = current_max_values
        
        # Return the maximum total value achievable
        return maximum_total_value

    maxValue = max_value
