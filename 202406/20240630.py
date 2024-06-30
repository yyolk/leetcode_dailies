# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of connected components

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.count -= 1
            return True
        return False

class Solution:
    """1579. Remove Max Number of Edges to Keep Graph Fully Traversable

    Alice and Bob have an undirected graph of `n` nodes and three types of edges:

    * Type 1: Can be traversed by Alice only.

    * Type 2: Can be traversed by Bob only.

    * Type 3: Can be traversed by both Alice and Bob.

    Given an array `edges` where `edges[i] = [typei, ui, vi]` represents a bidirectional
    edge of type `typei` between nodes `ui` and `vi`, find the maximum number of edges
    you can remove so that after removing the edges, the graph can still be fully
    traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if
    starting from any node, they can reach all other nodes.

    Return *the maximum number of edges you can remove, or return* `-1` *if Alice and
    Bob cannot fully traverse the graph.*

    """

    def max_num_edges_to_remove(self, n: int, edges: list[list[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        uf_combined = UnionFind(n)

        edges_removed = 0

        # Process type 3 edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                if not uf_combined.union(u - 1, v - 1):
                    edges_removed += 1
                else:
                    uf_alice.union(u - 1, v - 1)
                    uf_bob.union(u - 1, v - 1)

        # Process type 1 edges for Alice
        for edge_type, u, v in edges:
            if edge_type == 1:
                if not uf_alice.union(u - 1, v - 1):
                    edges_removed += 1

        # Process type 2 edges for Bob
        for edge_type, u, v in edges:
            if edge_type == 2:
                if not uf_bob.union(u - 1, v - 1):
                    edges_removed += 1

        # Check if both Alice and Bob can fully traverse the graph
        if uf_alice.count > 1 or uf_bob.count > 1:
            return -1

        return edges_removed

    maxNumEdgesToRemove = max_num_edges_to_remove
