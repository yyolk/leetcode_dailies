# https://leetcode.com/problems/minimum-time-difference/


class Solution:
    """539. Minimum Time Difference

    Given a list of 24\\-hour clock time points in **"HH:MM"** format, return *the
    minimum **minutes** difference between any two time\\-points in the list*.

    """

    def find_min_difference(self, time_points: list[str]) -> int:
        def time_to_minutes(time_str):
            """Convert time string to minutes since midnight."""
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes

        # Convert all times to minutes, handling 24:00 as 00:00
        times = [time_to_minutes(time) for time in time_points]
        # Handle 24:00
        times = [time if time < 24 * 60 else 0 for time in times]

        # Sort the times for easier calculation of differences
        times.sort()

        # Add the first time again to the end to handle wrap-around
        # Add 24 hours to the first time
        times.append(times[0] + 24 * 60)

        min_diff = float('inf')
        for i in range(len(times) - 1):
            # Calculate difference, considering wrap-around
            diff = times[i + 1] - times[i]
            min_diff = min(min_diff, diff)

        return min_diff

    findMinDifference = find_min_difference
