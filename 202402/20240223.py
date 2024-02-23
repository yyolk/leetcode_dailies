# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import heapq


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
        graph = {i: [] for i in range(n)}
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        # Priority queue to store (cost, current_city, stops_left)
        heap = [(0, src, k + 1)]
        
        # Dictionary to memoize the minimum cost for each (city, stops_left) pair
        memo = {}

        while heap:
            cost, current_city, stops_left = heapq.heappop(heap)

            # If the destination is reached, return the cost
            if current_city == dst:
                return cost

            # If stops are left, explore neighbors
            if stops_left > 0:
                for neighbor, price in graph[current_city]:
                    # Use memoization to avoid redundant computations
                    if (neighbor, stops_left - 1) not in memo or cost + price < memo[(neighbor, stops_left - 1)]:
                        heapq.heappush(heap, (cost + price, neighbor, stops_left - 1))
                        memo[(neighbor, stops_left - 1)] = cost + price

        # If destination is not reached within the given stops
        return -1

    findCheapestPrice = find_cheapest_price
