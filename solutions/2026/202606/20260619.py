# https://leetcode.com/problems/find-the-highest-altitude/


class Solution:
    """1732. Find the Highest Altitude

    There is a biker going on a road trip. The road trip consists of `n + 1` points at
    different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

    You are given an integer array `gain` of length `n` where `gain[i]` is the **net
    gain in altitude** between points `i`\u200b\u200b\u200b\u200b\u200b\u200b and `i + 1` for all (`0 <= i < n)`.
    Return *the **highest altitude** of a point.*

    Constraints:

    * `n == gain.length`

    * `1 <= n <= 100`

    * `-100 <= gain[i] <= 100`"""

    def largest_altitude(self, gain: list[int]) -> int: ...

    largestAltitude = largest_altitude
