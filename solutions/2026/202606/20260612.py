# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

from collections import deque


class Solution:
    """3559. Number of Ways to Assign Edge Weights II

    There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1.
    The tree is represented by a 2D integer array edges of length n-1, where
    edges[i]=[ui,vi] indicates edge between ui and vi. Initially all edges have
    weight 0. Assign each edge weight 1 or 2. The cost of a path between u and v
    is the total weight of edges in the path. For each queries[i]=[ui,vi], return
    the number of ways to assign weights to edges in the path such that the path
    cost is odd (mod 10^9+7). Disregard edges not in the path.
    """

    def assign_edge_weights(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        LOG = 18
        # build adjacency list for the tree
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # depth and binary lifting parent table
        depth = [0] * (n + 1)
        par = [[0] * (n + 1) for _ in range(LOG)]
        # BFS to compute depth and par[0] (iterative to avoid recursion limit)
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        par[0][1] = 1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    par[0][v] = u
                    q.append(v)
        # build binary lifting table
        for i in range(1, LOG):
            for j in range(1, n + 1):
                par[i][j] = par[i - 1][par[i - 1][j]]

        # LCA helper using binary lifting
        def get_lca(u: int, v: int) -> int:
            if depth[u] > depth[v]:
                u, v = v, u
            # lift v up to same depth as u
            diff = depth[v] - depth[u]
            for i in range(LOG):
                if diff & (1 << i):
                    v = par[i][v]
            if u == v:
                return u
            # lift both until just below LCA
            for i in range(LOG - 1, -1, -1):
                if par[i][u] != par[i][v]:
                    u = par[i][u]
                    v = par[i][v]
            return par[0][u]

        # process each query
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
            lca = get_lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[lca]
            # for k edges, exactly 2**(k-1) assignments make sum odd
            # (odd number of 1-weights, since 1=odd, 2=even)
            if k == 0:
                answer.append(0)
            else:
                answer.append(pow(2, k - 1, MOD))
        return answer

    assignEdgeWeights = assign_edge_weights
