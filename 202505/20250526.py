# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
from collections import deque


class Solution:
    """1857. Largest Color Value in a Directed Graph

    There is a **directed graph** of `n` colored nodes and `m` edges. The nodes are
    numbered from `0` to `n - 1`.

    You are given a string `colors` where `colors[i]` is a lowercase English letter
    representing the **color** of the `ith` node in this graph (**0-indexed**). You are
    also given a 2D array `edges` where `edges[j] = [aj, bj]` indicates that there is a
    **directed edge** from node `aj` to node `bj`.

    A valid **path** in the graph is a sequence of nodes `x1 -> x2 -> x3 -> ... -> xk`
    such that there is a directed edge from `xi` to `xi+1` for every `1 <= i < k`. The
    **color value** of the path is the number of nodes that are colored the **most
    frequently** occurring color along that path.

    Return *the **largest color value** of any valid path in the given graph, or* `-1`
    *if the graph contains a cycle*."""

    def largest_path_value(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)

        # Build adjacency list for outgoing edges and list for incoming edges
        adj_list = [[] for _ in range(n)]
        incoming_edges = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)  # a -> b (outgoing)
            incoming_edges[b].append(a)  # b <- a (incoming)

        # Compute indegree for each node
        indegree = [len(incoming_edges[i]) for i in range(n)]

        # Initialize queue with nodes having no incoming edges
        queue = deque([i for i in range(n) if indegree[i] == 0])

        # freq[node][c] is the max frequency of color c in paths ending at node
        freq = [[0] * 26 for _ in range(n)]
        max_freq = 0  # Tracks the largest color value
        processed = 0  # Counts nodes processed to detect cycles

        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            processed += 1

            # Convert current node's color to index (0-25)
            color_idx = ord(colors[node]) - ord("a")

            # Update frequency for each color
            for c in range(26):
                # Max frequency of color c from all predecessors
                max_pred = max([freq[pred][c] for pred in incoming_edges[node]] or [0])
                # Add 1 if current node's color matches c
                freq[node][c] = max_pred + (1 if c == color_idx else 0)

            # Update global maximum frequency
            max_freq = max(max_freq, max(freq[node]))

            # Process neighbors
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all nodes processed, there’s a cycle
        return max_freq if processed == n else -1

    largestPathValue = largest_path_value
