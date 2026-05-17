# https://leetcode.com/problems/reconstruct-itinerary/
from collections import defaultdict


class Solution:
    """332. Reconstruct Itinerary

    You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]` represent
    the departure and the arrival airports of one flight. Reconstruct the itinerary in order
    and return it.

    All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must
    begin with `"JFK"`. If there are multiple valid itineraries, you should return the
    itinerary that has the smallest lexical order when read as a single string.

    * For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK",
    "LGB"]`.

    You may assume all tickets form at least one valid itinerary. You must use all the
    tickets once and only once.
    """

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """Return the tickets provided in the correct order.

        Proposed solution using depth-first-search.

        Args:
            tickets (list of list of str): input tickets that are unsorted

        Returns:
            list of str: the reconstructed itinerary of the man who always
                departs from "JFK"
        """
        # Create a dictionary to represent the graph where keys are airports
        # and values are lists of airports reachable from the key airport.
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            graph[from_airport].append(to_airport)

        # Sort the lists of reachable airports in lexical order.
        for key in graph:
            graph[key].sort()

        # Initialize a list to store the result itinerary.
        result = []

        def dfs(node):
            """Depth-First Search"""
            while graph[node]:
                next_node = graph[node].pop(0)
                dfs(next_node)
            result.append(node)

        # Start the DFS from "JFK".
        dfs("JFK")

        # Reverse the result list to obtain the itinerary in the correct order.
        return result[::-1]
