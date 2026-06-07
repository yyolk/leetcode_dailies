# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
import heapq


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

    def min_time_to_reach(self, move_time: list[list[int]]) -> int:
        # Get grid dimensions
        n = len(move_time)
        m = len(move_time[0])

        # Initialize distance array: dist[i][j][p] is the minimum time to reach (i,j)
        # with parity p (0 for even number of moves, 1 for odd)
        dist = [[[float("inf")] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0  # Start at (0,0) at time 0 with 0 moves (even parity)

        # Priority queue to store states: (time, i, j, parity)
        heap = [(0, 0, 0, 0)]

        # Directions for adjacent moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, i, j, p = heapq.heappop(heap)

            # If this time is not the minimum for this state, skip
            if time > dist[i][j][p]:
                continue

            # Try moving to each adjacent room
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:  # Check bounds
                    # Move cost: 1 second if even moves so far, 2 if odd
                    move_cost = 1 if p == 0 else 2
                    # Must start move at or after move_time[ni][nj] and current time
                    t_start = max(time, move_time[ni][nj])
                    # Arrival time at new room
                    t_arrive = t_start + move_cost
                    # New parity flips since number of moves increases by 1
                    np = 1 - p

                    # If we found a faster way to reach (ni,nj) with parity np
                    if t_arrive < dist[ni][nj][np]:
                        dist[ni][nj][np] = t_arrive
                        heapq.heappush(heap, (t_arrive, ni, nj, np))

        # Return the minimum time to reach (n-1,m-1) with either parity
        return min(dist[n - 1][m - 1][0], dist[n - 1][m - 1][1])

    minTimeToReach = min_time_to_reach
