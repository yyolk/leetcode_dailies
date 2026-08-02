# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    """1344. Angle Between Hands of a Clock

    Given two numbers, hour and minutes, return the smaller angle (in degrees)
    formed between the hour and the minute hand. Answers within 1e-5 of the
    actual value will be accepted as correct.

    Constraints:
    * 1 <= hour <= 12
    * 0 <= minutes <= 59"""

    def angle_clock(self, hour: int, minutes: int) -> float:
        # Minute hand: 360/60 = 6.0 deg per minute
        min_pos = minutes * 6.0
        # Hour hand: (360/12)=30.0 per hour (hour % 12 for 12=0) + 0.5 per min
        hour_pos = (hour % 12) * 30.0 + minutes * 0.5
        # Absolute difference between the two hands
        diff = abs(hour_pos - min_pos)
        # Smaller angle is the min of diff and the other way around clock
        return min(diff, 360.0 - diff)

    angleClock = angle_clock
