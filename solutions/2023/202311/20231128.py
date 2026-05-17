# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
MOD = 10**9 + 7


class Solution:
    """2147. Number of Ways to Divide a Long Corridor

    Along a long library corridor, there is a line of seats and decorative plants. You
    are given a **0-indexed** string `corridor` of length `n` consisting of letters
    `'S'` and `'P'` where each `'S'` represents a seat and each `'P'` represents a
    plant.

    One room divider has **already** been installed to the left of index `0`, and
    **another** to the right of index `n - 1`. Additional room dividers can be
    installed. For each position between indices `i - 1` and `i` (`1 <= i <= n - 1`), at
    most one divider can be installed.

    Divide the corridor into non-overlapping sections, where each section has **exactly
    two seats** with any number of plants. There may be multiple ways to perform the
    division. Two ways are **different** if there is a position with a room divider
    installed in the first way but not in the second way.

    Return *the number of ways to divide the corridor*. Since the answer may be very
    large, return it **modulo** `109 + 7`. If there is no way, return `0`.
    """

    def number_of_ways(self, corridor: str) -> int:
        """Number of ways to divide to corridor.

        Args:
            corridor: 0-indexed string where 'S' and 'P' denote seat and plant
                respectively.

        Returns:
            The number of ways to divide the corridor, modulo 10^9 + 7.

        State variable explanation:
            x: Represents the number of ways to place dividers when the last seat
               encountered is part of a pair.
               (i.e., the number of ways when there are 0 seats counted so far)
            y: Represents the number of ways to place dividers when the last seat
               encountered is the first of a pair.
               (i.e., the number of ways when there is 1 seat counted so far).
            z: Represents the number of ways to place dividers when the last seat
               encountered is the second of a pair.
               (i.e., the number of ways when there are 2 seats counted so far).
        """
        # Initialize state variables
        x, y, z = 1, 0, 0

        # Iterate through the corridor
        for char in corridor:
            if char == "S":
                # When encountering a seat, update state variables.
                x, y, z = 0, x + z, y
            else:
                # When encountering a plant, update state variables.
                x, y, z = x + z, y, z

        # Return the result modulo MOD
        return z % MOD

    numberOfWays = number_of_ways
