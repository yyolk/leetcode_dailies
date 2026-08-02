# https://leetcode.com/problems/count-the-number-of-complete-components/


class Solution:
    """2685. Count the Number of Complete Components

    You are given an integer n. There is an undirected graph with n vertices,
    numbered from 0 to n-1. You are given a 2D integer array edges where
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
    vertices ai and bi.

    Return the number of complete connected components of the graph.

    A connected component is a subgraph of a graph in which there exists a path
    between any two vertices, and no vertex of the subgraph shares an edge with a
    vertex outside of the subgraph.

    A connected component is said to be complete if there exists an edge between
    every pair of its vertices.

    Constraints:
    * 1 <= n <= 50
    * 0 <= edges.length <= n * (n - 1) / 2
    * edges[i].length == 2
    * 0 <= ai, bi <= n - 1
    * ai != bi
    * There are no repeated edges.
    """

    def count_complete_components(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list for undirected graph
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n

        def dfs(node, comp):
            # DFS to collect all nodes in the connected component
            visited[node] = True
            comp.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        count = 0
        for i in range(n):
            if not visited[i]:
                # Collect nodes in this connected component
                comp = []
                dfs(i, comp)
                size = len(comp)
                # Complete if every node has degree size-1 (all neighbors inside)
                if all(len(adj[u]) == size - 1 for u in comp):
                    count += 1

        return count

    countCompleteComponents = count_complete_components
