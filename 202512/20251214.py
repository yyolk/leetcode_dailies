# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor


class Solution:
    """2147. Number of Ways to Divide a Long Corridor

    Along a long library corridor, there is a line of seats and decorative plants.
    You are given a 0-indexed string corridor of length n consisting of letters 'S'
    and 'P' where each 'S' represents a seat and each 'P' represents a plant.

    One room divider has already been installed to the left of index 0, and another
    to the right of index n - 1. Additional room dividers can be installed. For each
    position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can
    be installed.

    Divide the corridor into non-overlapping sections, where each section has exactly
    two seats with any number of plants. There may be multiple ways to perform the
    division. Two ways are different if there is a position with a room divider
    installed in the first way but not in the second way.

    Return the number of ways to divide the corridor. Since the answer may be very
    large, return it modulo 10**9 + 7. If there is no way, return 0.
    """
    def number_of_ways(self, corridor: str) -> int:
        # Define modulo constant
        MOD = 10**9 + 7
        
        # Collect positions of all seats
        pos = [i for i in range(len(corridor)) if corridor[i] == 'S']
        
        # Count total seats
        k = len(pos)
        
        # If no seats or odd number of seats, impossible to divide
        if k == 0 or k % 2 == 1:
            return 0
        
        # Number of sections (pairs of seats)
        m = k // 2
        
        # Initialize total ways to 1 (empty product)
        ways = 1
        
        # For each gap between consecutive pairs
        for j in range(m - 1):
            # Gap size: positions for divider between second seat of pair j and first seat of pair j+1
            gap = pos[2 * (j + 1)] - pos[2 * j + 1]
            # Multiply choices for this gap, modulo MOD
            ways = (ways * gap) % MOD
        
        # Return total number of ways
        return ways

    numberOfWays = number_of_ways