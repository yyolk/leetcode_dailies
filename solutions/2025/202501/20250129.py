# https://leetcode.com/problems/redundant-connection/


class Solution:
    """684. Redundant Connection

    In this problem, a tree is an **undirected graph** that is connected and has no
    cycles.

    You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`,
    with one additional edge added. The added edge has two **different** vertices chosen
    from `1` to `n`, and was not an edge that already existed. The graph is represented
    as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there
    is an edge between nodes `ai` and `bi` in the graph.

    Return *an edge that can be removed so that the resulting graph is a tree of* `n`
    *nodes*. If there are multiple answers, return the answer that occurs last in the
    input."""

    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        # 1-based indexing for nodes
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(u):
            while parent[u] != u:
                # Path compression
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return [u, v]
            # Union by rank
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1

        # The problem guarantees a cycle, so this line is theoretical
        return []

    findRedundantConnection = find_redundant_connection
