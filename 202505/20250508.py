# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/


class Solution:
    """3342. Find Minimum Time to Reach Last Room II

    There is a dungeon with `n x m` rooms arranged as a grid.

    You are given a 2D array `move_time` of size `n x m`, where `move_time[i][j]`
    represents the **minimum** time in seconds when you can **start moving** to that
    room. You start from the room `(0, 0)` at time `t = 0` and can move to an
    **adjacent** room. Moving between **adjacent** rooms takes one second for one move
    and two seconds for the next, **alternating** between the two.

    Return the **minimum** time to reach the room `(n - 1, m - 1)`.

    Two rooms are **adjacent** if they share a common wall, either *horizontally* or
    *vertically*."""

    def min_time_to_reach(self, move_time: list[list[int]]) -> int: ...

    minTimeToReach = min_time_to_reach
