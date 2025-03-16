# https://leetcode.com/problems/minimum-time-to-repair-cars/


class Solution:
    """2594. Minimum Time to Repair Cars

    You are given an integer array `ranks` representing the **ranks** of some mechanics.
    ranksi is the rank of the ith mechanic. A mechanic with a rank `r` can repair n cars
    in `r * n2` minutes.

    You are also given an integer `cars` representing the total number of cars waiting
    in the garage to be repaired.

    Return *the **minimum** time taken to repair all the cars.*

    **Note:** All the mechanics can repair the cars simultaneously."""

    def repair_cars(self, ranks: list[int], cars: int) -> int: ...

    repairCars = repair_cars
