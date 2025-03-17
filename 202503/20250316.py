# https://leetcode.com/problems/minimum-time-to-repair-cars/
from math import isqrt


class Solution:
    """2594. Minimum Time to Repair Cars

    You are given an integer array `ranks` representing the **ranks** of some mechanics.
    ranksi is the rank of the ith mechanic. A mechanic with a rank `r` can repair n cars
    in `r * n2` minutes.

    You are also given an integer `cars` representing the total number of cars waiting
    in the garage to be repaired.

    Return *the **minimum** time taken to repair all the cars.*

    **Note:** All the mechanics can repair the cars simultaneously."""

    def repair_cars(self, ranks: list[int], cars: int) -> int:
        def check(t: int, freq: list[int], cars: int) -> bool:
            # Calculate total cars repaired in time t across all ranks
            total = sum(freq[r] * isqrt(t // r) for r in range(1, 101) if freq[r] > 0)
            # Return True if enough cars can be repaired
            return total >= cars

        # Preprocess: build frequency map
        freq = [0] * 101  # Initialize frequency array for ranks 0-100
        for r in ranks:  # Count mechanics for each rank
            freq[r] += 1

        # Binary search on time
        lo, hi = 0, 10**14  # Set initial search range (0 to 10^14 minutes)
        while lo < hi:  # Continue until search range converges
            mid = (lo + hi) // 2  # Calculate midpoint of current range
            if check(mid, freq, cars):  # If mid time is sufficient
                hi = mid  # Search lower half
            else:  # If mid time is insufficient
                lo = mid + 1  # Search upper half
        return lo  # Return minimum time needed

    repairCars = repair_cars
