# https://leetcode.com/problems/modify-graph-edge-weights/
from heapq import heappop, heappush


class Solution:
    """2699. Modify Graph Edge Weights

    You are given an **undirected weighted** **connected** graph containing `n` nodes
    labeled from `0` to `n - 1`, and an integer array `edges` where `edges[i] = [ai, bi,
    wi]` indicates that there is an edge between nodes `ai` and `bi` with weight `wi`.

    Some edges have a weight of `-1` (`wi = -1`), while others have a **positive**
    weight (`wi > 0`).

    Your task is to modify **all edges** with a weight of `-1` by assigning them
    **positive integer values** in the range `[1, 2 * 109]` so that the **shortest
    distance** between the nodes `source` and `destination` becomes equal to an integer
    `target`. If there are **multiple** **modifications** that make the shortest
    distance between `source` and `destination` equal to `target`, any of them will be
    considered correct.

    Return *an array containing all edges (even unmodified ones) in any order if it is
    possible to make the shortest distance from* `source` *to* `destination` *equal to*
    `target`*, or an **empty array** if it's impossible.*

    **Note:** You are not allowed to modify the weights of edges with initial positive
    weights.

    """

    def modified_graph_edges(
        self, n: int, edges: list[list[int]], source: int, destination: int, target: int
    ) -> list[list[int]]:
        # Initialize the graph as an adjacency matrix
        graph = [[0] * n for _ in range(n)]
        for u, v, w in edges:
            # Populate the graph, setting undirected edges
            graph[u][v] = graph[v][u] = w

        # First Dijkstra run to find original shortest path with all edges
        orig = [float("inf")] * n
        orig[source] = 0
        # Priority queue for Dijkstra
        pq = [(0, source)]
        while pq:
            d, u = heappop(pq)
            if d == orig[u]:
                for v, w in enumerate(graph[u]):
                    # Only consider positive weights for the original path
                    if w and w != -1 and d + w < orig[v]:
                        orig[v] = d + w
                        heappush(pq, (orig[v], v))

        # If the original shortest path is already too short, it's impossible
        if orig[destination] < target:
            return []

        # If the original path length equals target, return edges with -1 set to max value
        if orig[destination] == target:
            ans = []
            for u, v, w in edges:
                # Max weight for unchanged -1 edges
                if w == -1:
                    w = 2_000_000_000
                ans.append([u, v, w])
            return ans

        # Second Dijkstra run to find path to modify
        dist = [float("inf")] * n
        dist[source] = 0
        parent = [-1] * n
        pq = [(0, source)]
        while pq:
            d, u = heappop(pq)

            if u == destination:
                # Stop when destination is reached
                break
            if d == dist[u]:
                for v, w in enumerate(graph[u]):
                    if w:
                        # If edge weight is -1, treat it as 1 for path finding
                        if w == -1:
                            dd = d + 1
                        else:
                            dd = d + w
                        if dd < dist[v]:
                            dist[v] = dd
                            parent[v] = u
                            heappush(pq, (dd, v))

        # If we can't reach the target even with modifications, return empty
        if d > target:
            return []

        # Modify the path back from destination to source
        u = destination
        while u >= 0:
            p = parent[u]
            if p >= 0:
                if graph[p][u] == -1:
                    if orig[p] < target:
                        # Set this edge to exactly what's needed to reach target from here
                        graph[p][u] = graph[u][p] = target - orig[p]
                        # This edge adjustment should be enough
                        break
                    else:
                        # Otherwise, set to minimum increment
                        graph[p][u] = graph[u][p] = 1
                # Adjust target for next edge consideration
                target -= graph[u][p]
            u = p

        # Construct the answer, converting any remaining -1 to max value
        ans = []
        for u, v, w in edges:
            if graph[u][v] == -1:
                graph[u][v] = 2_000_000_000
            ans.append([u, v, graph[u][v]])
        return ans

    modifiedGraphEdges = modified_graph_edges
