# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades

class Solution:
    """3600. Maximize Spanning Tree Stability with Upgrades

    You are given an integer n, representing n nodes numbered from 0 to n - 1
    and a list of edges, where edges[i] = [ui, vi, si, musti]: ui and vi
    indicates an undirected edge between nodes ui and vi. si is the strength
    of the edge. musti is an integer (0 or 1). If musti == 1, the edge must
    be included in the spanning tree. These edges cannot be upgraded. You are
    also given an integer k, the maximum number of upgrades you can perform.
    Each upgrade doubles the strength of an edge, and each eligible edge (with
    musti == 0) can be upgraded at most once. The stability of a spanning tree
    is defined as the minimum strength score among all edges included in it.
    Return the maximum possible stability of any valid spanning tree. If it is
    impossible to connect all nodes, return -1.
    Note: A spanning tree of a graph with n nodes is a subset of the edges
    that connects all nodes together (i.e. the graph is connected) without
    forming any cycles, and uses exactly n - 1 edges.
    """
    def max_stability(self, n: int, edges: list[list[int]], k: int) -> int:
        # Pre-check must edges for cycles (independent of stability)
        parent = list(range(n))
        rank = [0] * n
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x: int, y: int) -> bool:
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        for u, v, s, m in edges:
            if m == 1 and not union(u, v):
                return -1
        # Upper bound for binary search
        max_s = max((s for _, _, s, _ in edges), default=0)

        def can_achieve(x: int) -> bool:
            # Fresh UF and component count for this stability check
            parent = list(range(n))
            rank = [0] * n
            def find(x: int) -> int:
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            def union(x: int, y: int) -> bool:
                px = find(x)
                py = find(y)
                if px == py:
                    return False
                if rank[px] < rank[py]:
                    parent[px] = py
                elif rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[py] = px
                    rank[px] += 1
                return True
            comp = n
            # Add all must edges (fixed, cannot upgrade)
            for u, v, s, m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if union(u, v):
                        comp -= 1
            # Add optional edges usable without upgrade (s >= x)
            for u, v, s, m in edges:
                if m == 0 and s >= x:
                    if union(u, v):
                        comp -= 1
            if comp == 1:
                return True
            # Minimum upgrades required equals remaining components - 1
            needed = comp - 1
            if needed > k:
                return False
            # Add optional edges usable only with upgrade (2 * s >= x)
            for u, v, s, m in edges:
                if m == 0 and s < x and 2 * s >= x:
                    if union(u, v):
                        comp -= 1
            return comp == 1

        # Binary search maximizes the minimum edge strength
        left = 0
        right = 2 * max_s
        while left < right:
            mid = (left + right + 1) // 2
            if can_achieve(mid):
                left = mid
            else:
                right = mid - 1
        return left if can_achieve(left) else -1

    maxStability = max_stability