# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution:
    """3633. Earliest Finish Time for Land and Water Rides I
    
    You are given two categories of theme park attractions: land rides and water
    rides.
    * Land rides
      + land_start_time[i] – the earliest time the ith land ride can be boarded.
      + land_duration[i] – how long the ith land ride lasts.
    * Water rides
      + water_start_time[j] – the earliest time the jth water ride can be
        boarded.
      + water_duration[j] – how long the jth water ride lasts.
    A tourist must experience exactly one ride from each category, in either
    order.
    * A ride may be started at its opening time or any later moment.
    * If a ride is started at time t, it finishes at time t + duration.
    * Immediately after finishing one ride the tourist may board the other (if it
      is already open) or wait until it opens.
    Return the earliest possible time at which the tourist can finish both rides.
    """
    def earliest_finish_time(
        self,
        land_start_time: list[int],
        land_duration: list[int],
        water_start_time: list[int],
        water_duration: list[int],
    ) -> int:
        # always pair with the land that finishes earliest when doing land first
        min_land_finish = min(
            ls + ld for ls, ld in zip(land_start_time, land_duration)
        )
        # always pair with the water that finishes earliest when doing water first
        min_water_finish = min(
            ws + wd for ws, wd in zip(water_start_time, water_duration)
        )
        # land-first min over all water rides
        land_first = min(
            max(min_land_finish + wd, ws + wd)
            for ws, wd in zip(water_start_time, water_duration)
        )
        # water-first min over all land rides
        water_first = min(
            max(min_water_finish + ld, ls + ld)
            for ls, ld in zip(land_start_time, land_duration)
        )
        # overall minimum finish time across both possible orders
        return min(land_first, water_first)

    earliestFinishTime = earliest_finish_time