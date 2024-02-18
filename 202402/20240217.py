# https://leetcode.com/problems/furthest-building-you-can-reach/


class Solution:
    """1642. Furthest Building You Can Reach

    You are given an integer array `heights` representing the heights of buildings, some
    `bricks`, and some `ladders`.

    You start your journey from building `0` and move to the next building by possibly
    using bricks or ladders.

    While moving from building `i` to building `i+1` (**0-indexed**),

    * If the current building's height is **greater than or equal** to the next
    building's height, you do **not** need a ladder or bricks.

    * If the current building's height is **less than** the next building's height, you
    can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

    *Return the furthest building index (0-indexed) you can reach if you use the given
    ladders and bricks optimally.*

    """

    def furthest_building(self, heights: list[int], bricks: int, ladders: int) -> int:
        min_heap = []  # A min heap to store the heights difference
        bricks_used = 0

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                heapq.heappush(min_heap, diff)

                # If the number of elements in the heap exceeds the available ladders,
                # use bricks instead of ladders.
                if len(min_heap) > ladders:
                    bricks_used += heapq.heappop(min_heap)

                # If the total bricks used exceeds the available bricks, return the current index.
                if bricks_used > bricks:
                    return i

        # If we reach the end of the buildings, we can reach the furthest building.
        return len(heights) - 1

    furthestBuilding = furthest_building
