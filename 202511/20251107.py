# https://leetcode.com/problems/maximize-the-minimum-powered-city/


class Solution:
    """2528. Maximize the Minimum Powered City

    You are given a 0-indexed integer array stations of length n, where
    stations[i] represents the number of power stations in the ith city.

    Each power station can provide power to every city in a fixed range. In
    other words, if the range is denoted by r, then a power station at city i
    can provide power to all cities j such that |i - j| <= r and 0 <= i, j <=
    n - 1.

    Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 -
    10| = 7.

    The power of a city is the total number of power stations it is being
    provided power from.

    The government has sanctioned building k more power stations, each of
    which can be built in any city, and have the same range as the
    pre-existing ones.

    Given the two integers r and k, return the maximum possible minimum power
    of a city, if the additional power stations are built optimally.

    Note that you can build the k power stations in multiple cities.
    """
    def max_power(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        # Difference array with extra space for safety
        df = [0] * (n + 1)
        # Build the difference array for initial powers
        for i in range(n):
            # Add stations[i] to the start of its coverage
            df[max(0, i - r)] += stations[i]
            # Subtract stations[i] after the end of its coverage
            end = min(n - 1, i + r) + 1
            if end < n + 1:
                df[end] -= stations[i]
        # Compute the minimum initial power
        initial_min = float('inf')
        cur = 0
        for i in range(n):
            cur += df[i]
            initial_min = min(initial_min, cur)
        # Binary search bounds: low is initial min, high is a large number
        low = initial_min
        high = 10**12  # Sufficiently large upper bound
        # Binary search for the maximum achievable minimum power
        while low < high:
            # Midpoint biased towards higher
            mid = (low + high + 1) // 2
            # Check if mid is achievable
            if self._can_achieve(df, n, r, k, mid):
                low = mid
            else:
                high = mid - 1
        return low

    def _can_achieve(self, df: list[int], n: int, r: int, k: int, target: int) -> bool:
        # Copy the difference array
        diff = df[:]
        # Current power prefix sum
        cur = 0
        # Total added stations
        total_added = 0
        for i in range(n):
            # Accumulate the difference to get current power
            cur += diff[i]
            # If current power is below target
            if cur < target:
                # Calculate needed additions
                need = target - cur
                # Accumulate total added
                total_added += need
                # Early exit if exceeded k
                if total_added > k:
                    return False
                # Update current to target
                cur = target
                # Subtract the need after the coverage range (i to i+2r)
                end = min(n - 1, i + 2 * r) + 1
                if end < n + 1:
                    diff[end] -= need
        return True

    maxPower = max_power