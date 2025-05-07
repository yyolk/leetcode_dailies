# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/


class Solution:
    """3341. Find Minimum Time to Reach Last Room I

    There is a dungeon with `n x m` rooms arranged as a grid.

    You are given a 2D array `move_time` of size `n x m`, where `move_time[i][j]`
    represents the **minimum** time in seconds when you can **start moving** to that
    room. You start from the room `(0, 0)` at time `t = 0` and can move to an
    **adjacent** room. Moving between adjacent rooms takes *exactly* one second.

    Return the **minimum** time to reach the room `(n - 1, m - 1)`.

    Two rooms are **adjacent** if they share a common wall, either *horizontally* or
    *vertically*."""

    def min_time_to_reach(self, move_time: list[list[int]]) -> int:
        # Get grid dimensions
        n = len(move_time)
        m = len(move_time[0])
        
        # Handle edge case (though constraints typically ensure n, m >= 1)
        if n == 0 or m == 0:
            return 0
        
        # Initialize distance array with infinity
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0  # Starting position at time 0
        
        # Priority queue: (time, row, col)
        heap = [(0, 0, 0)]
        
        # Possible directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            # Get the room with the smallest time
            t, i, j = heapq.heappop(heap)
            
            # If we've found a better path to this room already, skip
            if t > dist[i][j]:
                continue
            
            # If we reached the target, return the time
            if i == n - 1 and j == m - 1:
                return t
            
            # Explore adjacent rooms
            for di, dj in directions:
                p, q = i + di, j + dj
                # Check if the new position is within bounds
                if 0 <= p < n and 0 <= q < m:
                    # Calculate arrival time to (p, q)
                    arrival = max(t, move_time[p][q]) + 1
                    # If we found a faster way to reach (p, q), update it
                    if arrival < dist[p][q]:
                        dist[p][q] = arrival
                        heapq.heappush(heap, (arrival, p, q))
        
        # Should always be reachable in a grid without obstacles
        return dist[n-1][m-1]

    minTimeToReach = min_time_to_reach
