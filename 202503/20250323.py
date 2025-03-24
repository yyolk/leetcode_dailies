# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
import heapq

# Define modulo constant
MOD = 10**9 + 7


class Solution:
    """1976. Number of Ways to Arrive at Destination

    You are in a city that consists of `n` intersections numbered from `0` to `n - 1`
    with **bi-directional** roads between some intersections. The inputs are generated
    such that you can reach any intersection from any other intersection and that there
    is at most one road between any two intersections.

    You are given an integer `n` and a 2D integer array `roads` where `roads[i] = [ui,
    vi, timei]` means that there is a road between intersections `ui` and `vi` that
    takes `timei` minutes to travel. You want to know in how many ways you can travel
    from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

    Return *the **number of ways** you can arrive at your destination in the **shortest
    amount of time***. Since the answer may be large, return it **modulo** `109 + 7`."""

    def count_paths(self, n: int, roads: list[list[int]]) -> int:
        # Build adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))  # Bi-directional

        # Initialize distance and ways arrays
        dist = [float("inf")] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1

        # Priority queue: (distance, node)
        pq = [(0, 0)]
        # Visited array to mark processed nodes
        visited = [False] * n

        # Process nodes with Dijkstra's algorithm
        while pq:
            dist_u, u = heapq.heappop(pq)
            # Skip if already visited (distance finalized)
            if visited[u]:
                continue
            visited[u] = True

            # Explore neighbors
            for v, time in adj[u]:
                new_time = dist[u] + time
                if new_time < dist[v]:
                    # Found a shorter path
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_time, v))
                elif new_time == dist[v]:
                    # Found another path with the same shortest time
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]

    countPaths = count_paths
