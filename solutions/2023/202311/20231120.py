# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/


class Solution:
    """2391. Minimum Amount of Time to Collect Garbage

    You are given a **0-indexed** array of strings `garbage` where `garbage[i]`
    represents the assortment of garbage at the `ith` house. `garbage[i]` consists only
    of the characters `'M'`, `'P'` and `'G'` representing one unit of metal, paper and
    glass garbage respectively. Picking up **one** unit of any type of garbage takes `1`
    minute.

    You are also given a **0-indexed** integer array `travel` where `travel[i]` is the
    number of minutes needed to go from house `i` to house `i + 1`.

    There are three garbage trucks in the city, each responsible for picking up one type
    of garbage. Each garbage truck starts at house `0` and must visit each house **in
    order**; however, they do **not** need to visit every house.

    Only **one** garbage truck may be used at any given moment. While one truck is
    driving or picking up garbage, the other two trucks **cannot** do anything.

    Return *the **minimum** number of minutes needed to pick up all the garbage.*
    """

    def garbage_collection(self, garbage: list[str], travel: list[int]) -> int:
        """The minimum number of minutes needed to pick up all the garbage.

        Args:
            garbage: 0-indexed list of strings where the ith element is the ith house.
            travel: 0-index integer list with the time it takes to go from house i to
                house i + 1.

        Returns:
            The minimum number of minutes needed to pick up all the garbage
        """
        n = len(garbage)
        time_g, time_p, time_m = 0, 0, 0
        time_total = 0

        # Iterate through each house in reverse order.
        for i in range(n - 1, -1, -1):
            x = garbage[i]
            time_total += len(x)

            # Update the last occurrence of each type of garbage.
            if time_g == 0 and "G" in x:
                time_g = i
            if time_p == 0 and "P" in x:
                time_p = i
            if time_m == 0 and "M" in x:
                time_m = i

        # Update the total time with the travel time for each garbage type.
        time_total += sum(travel[:time_g]) + sum(travel[:time_p]) + sum(travel[:time_m])

        return time_total

    garbageCollection = garbage_collection
