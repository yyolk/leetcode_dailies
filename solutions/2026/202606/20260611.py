# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

from collections import deque


class Solution:
    """3558. Number of Ways to Assign Edge Weights I

    There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1.
    The tree is represented by a 2D integer array edges of length n-1, where
    edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
    Initially, all edges have a weight of 0. You must assign each edge a weight of
    either 1 or 2.
    The cost of a path between any two nodes u and v is the total weight of all
    edges in the path connecting them.
    Select any one node x at the maximum depth. Return the number of ways to
    assign edge weights in the path from node 1 to x such that its total cost is
    odd.
    Since the answer may be large, return it modulo 109 + 7.
    Note: Ignore all edges not in the path from node 1 to x.
    Constraints:
    * 2 <= n <= 105
    * edges.length == n - 1
    * edges[i] == [ui, vi]
    * 1 <= ui, vi <= n
    * edges represents a valid tree.
    """

    def assign_edge_weights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        # Build undirected adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS from root 1 to compute max depth (edge count)
        q = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        max_d = 0
        while q:
            node, d = q.popleft()
            max_d = max(max_d, d)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, d + 1))

        # Path to x at max depth has max_d edges.
        # Sum odd iff odd number of 1-weights (2 is even).
        # Exactly half of 2**max_d assignments yield odd sum.
        MOD = 10**9 + 7
        return pow(2, max_d - 1, MOD)

    assignEdgeWeights = assign_edge_weights
