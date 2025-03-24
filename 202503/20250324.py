# https://leetcode.com/problems/count-days-without-meetings/


class Solution:
    """3169. Count Days Without Meetings

    You are given a positive integer `days` representing the total number of days an
    employee is available for work (starting from day 1). You are also given a 2D array
    `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the
    starting and ending days of meeting `i` (inclusive).

    Return the count of days when the employee is available for work but no meetings are
    scheduled.

    **Note:** The meetings may overlap."""

    def count_days(self, days: int, meetings: list[list[int]]) -> int:
        # If there are no meetings, all days are free
        if not meetings:
            return days
        
        # Sort meetings by start day to process them sequentially
        meetings.sort()
        
        # Initialize variables to track total covered days and current merged interval
        covered = 0
        current_start = meetings[0][0]
        current_end = meetings[0][1]
        
        # Iterate through meetings starting from the second one
        for meeting in meetings[1:]:
            if meeting[0] <= current_end:
                # If the current meeting overlaps with the merged interval,
                # extend the end to the maximum of current end and meeting's end
                current_end = max(current_end, meeting[1])
            else:
                # If there's no overlap, add the length of the current merged interval
                # to covered days and start a new interval with the current meeting
                covered += current_end - current_start + 1
                current_start = meeting[0]
                current_end = meeting[1]
        
        # Add the last merged interval to the total covered days
        covered += current_end - current_start + 1
        
        # Return the number of free days by subtracting covered days from total days
        return days - covered

    countDays = count_days
