# https://leetcode.com/problems/avoid-flood-in-the-city/
import heapq

from collections import defaultdict


class Solution:
    """1488. Avoid Flood in The City

    Your country has an infinite number of lakes. Initially, all the lakes are empty,
    but when it rains over the `nth` lake, the `nth` lake becomes full of water. If it
    rains over a lake that is **full of water**, there will be a **flood**. Your goal is
    to avoid floods in any lake.

    Given an integer array `rains` where:

    * `rains[i] > 0` means there will be rains over the `rains[i]` lake.

    * `rains[i] == 0` means there are no rains this day and you can choose **one lake**
    this day and **dry it**.

    Return *an array `ans`* where:

    * `ans.length == rains.length`

    * `ans[i] == -1` if `rains[i] > 0`.

    * `ans[i]` is the lake you choose to dry in the `ith` day if `rains[i] == 0`.

    If there are multiple valid answers return **any** of them. If it is impossible to
    avoid flood return **an empty array**.

    Notice that if you chose to dry a full lake, it becomes empty, but if you chose to
    dry an empty lake, nothing changes."""

    def avoid_flood(self, rains: list[int]) -> list[int]:
        # Determine the number of days
        n = len(rains)
        # Initialize the answer list with placeholders
        ans = [0] * n
        # Map each lake to the list of days it rains
        lake_to_days = defaultdict(list)
        for i in range(n):
            if rains[i] > 0:
                lake_to_days[rains[i]].append(i)
        # Track the next rain index for each lake
        next_idx = defaultdict(int)
        # Set of currently full lakes
        full = set()
        # Min-heap for (next_rain_day, lake) of full lakes with future rains
        heap = []
        for i in range(n):
            if rains[i] > 0:
                lake = rains[i]
                # Check if raining on a full lake causes flood
                if lake in full:
                    return []
                # Mark the lake as full
                full.add(lake)
                # Set answer for rainy day
                ans[i] = -1
                # Get the rain days for this lake
                days = lake_to_days[lake]
                # Current index in rain days
                idx = next_idx[lake]
                # Advance index past current day if matching
                if idx < len(days) and days[idx] == i:
                    next_idx[lake] += 1
                # Update index after advance
                idx = next_idx[lake]
                # If there is a future rain, add to heap
                if idx < len(days):
                    heapq.heappush(heap, (days[idx], lake))
            else:
                # Handle dry day
                if heap:
                    # Get the lake with the soonest next rain
                    next_day, lake = heapq.heappop(heap)
                    # Set to dry this lake
                    ans[i] = lake
                    # Remove from full lakes
                    full.remove(lake)
                else:
                    # No urgent lake, dry any (e.g., lake 1)
                    ans[i] = 1
        return ans

    avoidFlood = avoid_flood
