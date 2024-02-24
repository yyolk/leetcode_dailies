# https://leetcode.com/problems/cheapest-flights-within-k-stops/
from collections import defaultdict
from queue import Queue


class Solution:
    """787. Cheapest Flights Within K Stops

    There are `n` cities connected by some number of flights. You are given an array
    `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight
    from city `fromi` to city `toi` with cost `pricei`.

    You are also given three integers `src`, `dst`, and `k`, return ***the cheapest
    price** from* `src` *to* `dst` *with at most* `k` *stops.* If there is no such
    route, return`-1`.

    """

    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # Create an adjacency list to represent the graph
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        # Initialize distances with infinity, except for source node which is set to 0
        dist = [float("inf")] * n
        dist[src] = 0

        # Use a queue for BFS traversal
        q = Queue()
        q.put((src, 0))
        stops = 0

        # Perform BFS with a maximum of k stops
        while not q.empty() and stops <= k:
            sz = q.qsize()
            for _ in range(sz):
                node, distance = q.get()

                # Skip if node has no outgoing flights
                if node not in adj:
                    continue

                # Explore neighbors
                for neighbour, price in adj[node]:
                    # Update distance if a shorter path is found
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.put((neighbour, dist[neighbour]))

            stops += 1

        # Return the minimum cost to reach the destination, or -1 if unreachable
        return dist[dst] if dist[dst] != float("inf") else -1

    findCheapestPrice = find_cheapest_price
