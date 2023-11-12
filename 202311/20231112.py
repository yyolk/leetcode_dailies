# https://leetcode.com/problems/bus-routes/
from collections import defaultdict, deque


class Solution:
    """815. Bus Routes

    You are given an array `routes` representing bus routes where `routes[i]` is a bus
    route that the `ith` bus repeats forever.

    * For example, if `routes[0] = [1, 5, 7]`, this means that the `0th` bus travels in
    the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

    You will start at the bus stop `source` (You are not on any bus initially), and you
    want to go to the bus stop `target`. You can travel between bus stops by buses only.

    Return *the least number of buses you must take to travel from* `source` *to*
    `target`. Return `-1` if it is not possible.
    """

    def num_buses_to_destination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        """
        Returns the least number of buses you must take to travel from the source bus
        stop to the target bus stop.

        Args:
            routes: A list of bus routes where routes[i] is a list representing the
                stops of the i_th bus.
            source: The bus stop where the journey starts.
            target: The bus stop where the journey ends.

        Returns:
            The minimum number of buses needed to travel from the source to the target
            bus stop. Returns -1 if not possible.
        """

        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        visited_routes = set()
        visited_stops = set()

        queue = deque([(source, 0)])

        while queue:
            current_stop, num_buses = queue.popleft()

            if current_stop == target:
                return num_buses

            for route_index in stop_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, num_buses + 1))

        return -1

    numBusesToDestination = num_buses_to_destination
