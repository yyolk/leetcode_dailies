# https://leetcode.com/problems/power-grid-maintenance/
import heapq
from collections import defaultdict


class Solution:
    """3607. Power Grid Maintenance

    You are given an integer c representing c power stations, each with a unique
    identifier id from 1 to c (1-based indexing).

    These stations are interconnected via n bidirectional cables, represented by a
    2D array connections, where each element connections[i] = [ui, vi] indicates a
    connection between station ui and station vi. Stations that are directly or
    indirectly connected form a power grid.

    Initially, all stations are online (operational).

    You are also given a 2D array queries, where each query is one of the following
    two types:

    [1, x]: A maintenance check is requested for station x. If station x is
    online, it resolves the check by itself. If station x is offline, the check is
    resolved by the operational station with the smallest id in the same power grid
    as x. If no operational station exists in that grid, return -1.

    [2, x]: Station x goes offline (i.e., it becomes non-operational).

    Return an array of integers representing the results of each query of type
    [1, x] in the order they appear.

    Note: The power grid preserves its structure; an offline (nonoperational) node
    remains part of its grid and taking it offline does not alter connectivity.
    """
    def process_queries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Disjoint Set Union for finding connected components
        class DSU:
            def __init__(self, n: int):
                self.p = list(range(n + 1))

            def find(self, x: int) -> int:
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x: int, y: int) -> None:
                px, py = self.find(x), self.find(y)
                if px != py:
                    self.p[px] = py

        dsu = DSU(c)
        # Union all connections to build components
        for u, v in connections:
            dsu.union(u, v)

        # Group stations by their component root
        components = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            components[root].append(i)

        # Create min-heaps for each component's stations
        heaps = {}
        for root, members in components.items():
            heaps[root] = members[:]
            heapq.heapify(heaps[root])

        # Track online status (index 1 to c)
        online = [False] + [True] * c

        res = []
        for q in queries:
            typ, x = q[0], q[1]
            if typ == 2:
                # Set station offline
                online[x] = False
            else:
                # Type 1 query
                if online[x]:
                    # If x online, return x
                    res.append(x)
                else:
                    # Find min online in component
                    root = dsu.find(x)
                    h = heaps[root]
                    # Remove offline stations from heap front
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    if h:
                        res.append(h[0])
                    else:
                        res.append(-1)
        return res

    processQueries = process_queries