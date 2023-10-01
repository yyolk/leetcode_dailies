# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/


class UnionFind:
    """A data structure for disjoint-set union (Union-Find).

    This class allows efficient operations to group elements into sets and determine
    whether two elements belong to the same set. It uses the Union-Find algorithm
    with path compression and union by rank for optimized performance.

    Attributes:
        parent (List of int): An array where each element represents the parent
        of the corresponding element, initialized as the element itself.

    Methods:
        find(x): Find the representative (root) element of the set containing x.
        union(x, y): Merge the sets containing elements x and y, if they are not
        already in the same set.
    """

    def __init__(self, n):
        """Initialize a UnionFind instance with 'n' elements."""
        self.parent = list(range(n))

    def find(self, x):
        """Find the representative (root) element of the set containing 'x'.

        Args:
            x (int): The element to find the representative of

        Returns:
            int: The representative (root) element of the set containing 'x'
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Merge the sets containing elements 'x' and 'y', if they are not already in the same set.

        Args:
            x (int): The first element.
            y (int): The second element.

        Returns:
            bool: True if 'x' and 'y' were in different sets and were merged,
            False if they were already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        return True


class Solution:
    """1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

    Given a weighted undirected connected graph with n vertices numbered from `0` to
    `n - 1`, and an array `edges` where `edges[i] = [ai, bi, weighti]` represents a
    bidirectional and weighted edge between nodes `ai` and `bi`. A minimum spanning
    tree (MST) is a subset of the graph's edges that connects all vertices without
    cycles and with the minimum possible total edge weight.

    Find *all the critical and pseudo-critical edges in the given graph's minimum
    spanning tree (MST)*. An MST edge whose deletion from the graph would cause the MST
    weight to increase is called a *critical edge*. On the other hand, a
    pseudo-critical edge is that which can appear in some MSTs but not all.

    Note that you can return the indices of the edges in any order.
    """

    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        """Finds critical and pseudo critical edges weight

        Proposed solution using Kruskal's Algorithm

        Args:
            n: (int): The number of verticies in the graph.
            edges (List of List of int): The input edges of the minimum spanning tree

        Returns:
            List of List of int: The critical and pseudo critical edges in a
            two item List of List of int.
        """

        def kruskal(n, edges, included_edges, e):
            """Implmentation of Kruskal's algorithm"""
            uf = UnionFind(n)
            total_weight = 0
            mst = []
            if e != -1:
                total_weight += edges[e][2]
                uf.union(edges[e][0], edges[e][1])

            # Discard idx
            for i, (a, b, w, _) in enumerate(edges):
                if i == included_edges:
                    continue
                if uf.find(edges[i][0]) == uf.find(edges[i][1]):
                    continue
                if uf.union(a, b):
                    mst.append([a, b, w])
                    total_weight += w
            for i in range(n):
                if uf.find(i) != uf.find(0):
                    return mst, float("inf")
            return mst, total_weight

        edges_with_indices = [(a, b, w, i) for i, (a, b, w) in enumerate(edges)]
        edges_with_indices.sort(key=lambda x: x[2])

        critical = []
        pseudo_critical = []

        # Discard mst, keep mst_weight
        _, mst_weight = kruskal(n, edges_with_indices, -1, -1)

        # Discard a, b, w from each edge
        for i, (_, _, _, idx) in enumerate(edges_with_indices):
            # Discard mst, find weight with and without edge
            _, weight_without_edge = kruskal(n, edges_with_indices, i, -1)
            _, weight_with_edge = kruskal(n, edges_with_indices, -1, i)
            # Compare mst_weight to weight with and without edge
            if mst_weight < weight_without_edge:
                # Removing this edge increases MST weight, so it's critical
                critical.append(idx)
            elif mst_weight == weight_with_edge:
                # Removing this edge doesn't change MST weight, so it's pseudo-critical
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]
