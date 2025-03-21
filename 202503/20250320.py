# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/


class Solution:
    """3108. Minimum Cost Walk in Weighted Graph

    There is an undirected weighted graph with `n` vertices labeled from `0` to `n - 1`.

    You are given the integer `n` and an array `edges`, where `edges[i] = [ui, vi, wi]`
    indicates that there is an edge between vertices `ui` and `vi` with a weight of
    `wi`.

    A walk on a graph is a sequence of vertices and edges. The walk starts and ends with
    a vertex, and each edge connects the vertex that comes before it and the vertex that
    comes after it. It's important to note that a walk may visit the same edge or vertex
    more than once.

    The **cost** of a walk starting at node `u` and ending at node `v` is defined as the
    bitwise `AND` of the weights of the edges traversed during the walk. In other words,
    if the sequence of edge weights encountered during the walk is `w0, w1, w2, ...,
    wk`, then the cost is calculated as `w0 & w1 & w2 & ... & wk`, where `&` denotes the
    bitwise `AND` operator.

    You are also given a 2D array `query`, where `query[i] = [si, ti]`. For each query,
    you need to find the minimum cost of the walk starting at vertex `si` and ending at
    vertex `ti`. If there exists no such walk, the answer is `-1`.

    Return *the array* `answer`*, where* `answer[i]` *denotes the **minimum** cost of a
    walk for query* `i`."""

    def minimum_cost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        # Union-Find helper functions
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])  # Path compression
            return parent[x]

        def union(parent, rank, x, y):
            px = find(parent, x)
            py = find(parent, y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        # Initialize Union-Find data structures
        parent = [i for i in range(n)]
        rank = [0] * n

        # Step 1: Build connected components using all edges
        for u, v, _ in edges:
            union(parent, rank, u, v)

        # Step 2: Precompute the root for each vertex for efficiency
        root = [find(parent, i) for i in range(n)]

        # Step 3: Compute the AND of all edge weights for each component
        and_value = [-1] * n  # -1 means all bits set, neutral for AND
        for u, v, w in edges:
            r = root[u]  # Root of the component containing u (and v)
            and_value[r] &= w

        # Step 4: Process each query
        answer = []
        for s, t in query:
            if root[s] == root[t]:
                answer.append(
                    and_value[root[s]]
                )  # Minimum cost is the AND of the component
            else:
                answer.append(-1)  # No walk exists between different components

        return answer

    minimumCost = minimum_cost
