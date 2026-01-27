# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals
import heapq


class Solution:
    """3650. Minimum Cost Path with Edge Reversals
    
    You are given a directed, weighted graph with n nodes labeled from 0 to n - 1,
    and an array edges where edges[i] = [ui, vi, wi] represents a directed edge
    from node ui to node vi with cost wi.
    Each node has a switch usable at most once: you may reverse one incoming edge
    and immediately traverse the reversal at cost 2 * wi.
    Return the minimum cost from node 0 to node n-1, or -1 if impossible.
    """
    def min_cost(self, n: int, edges: list[list[int]]) -> int:
        # Augmented graph: for each original u->v w, add u->v w and v->u 2*w
        # The 2*w edges model using the switch at the arrival node (or start)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        # Dijkstra on the augmented graph
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, node = heapq.heappop(pq)
            if cost > dist[node]:
                continue
            for nei, wc in graph[node]:
                new_cost = cost + wc
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        return dist[n-1] if dist[n-1] < INF else -1

    minCost = min_cost