# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

import heapq


class Solution:
    """3970. Shortest Path With At Most K Consecutive Identical Characters

    You are given an integer `n` representing the number of nodes in a
    **directed weighted** graph, numbered from 0 to `n - 1`. This is
    represented by a 2D integer array `edges`, where `edges[i] = [ui, vi, wi]`
    represents a directed edge from node `ui` to node `vi` with weight `wi`.

    You are also given a string `labels` of length `n`, where `labels[i]` is
    the character assigned to node `i`, and an integer `k`.

    Return the **minimum** **total** edge weight of a path from node 0 to node
    `n - 1` such that the concatenation of the labels of the nodes along the
    path contains **at most** `k` **consecutive** **identical** characters. If
    no valid path exists, return -1.

    Constraints:

    * `1 <= n == labels.length <= 5 * 10^4`

    * `0 <= edges.length <= 5 * 10^4`

    * `edges[i] == [ui, vi, wi]`

    * `0 <= ui, vi <= n - 1`

    * `ui != vi`

    * `1 <= wi <= 10^4`

    * `labels` consists of lowercase English letters

    * `1 <= k <= 50`
    """

    def shortest_path(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build adjacency list of (neighbor, weight) pairs.
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][cnt]: min cost to reach node with ending streak length cnt.
        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(n)]
        # Start at node 0 with its own label counted as consecutive 1.
        dist[0][1] = 0
        # Min-heap of (cost, node, consecutive_count).
        pq: list[tuple[int, int, int]] = [(0, 0, 1)]

        while pq:
            cost, u, cnt = heapq.heappop(pq)
            # Skip if a better path to this state was already found.
            if cost > dist[u][cnt]:
                continue
            # First time we pop the target, it is the shortest valid path.
            if u == n - 1:
                return cost
            for v, w in adj[u]:
                # Extend streak if labels match, otherwise reset to 1.
                new_cnt = cnt + 1 if labels[u] == labels[v] else 1
                if new_cnt > k:
                    continue
                new_cost = cost + w
                if new_cost < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_cnt))

        return -1

    shortestPath = shortest_path
