# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
from collections import deque


class Solution:
    """3373. Maximize the Number of Target Nodes After Connecting Trees II

    There exist two **undirected** trees with `n` and `m` nodes, labeled from `[0, n -
    1]` and `[0, m - 1]`, respectively.

    You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m
    - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge
    between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates
    that there is an edge between nodes `ui` and `vi` in the second tree.

    Node `u` is **target** to node `v` if the number of edges on the path from `u` to
    `v` is even. **Note** that a node is *always* **target** to itself.

    Return an array of `n` integers `answer`, where `answer[i]` is the **maximum**
    possible number of nodes that are **target** to node `i` of the first tree if you
    had to connect one node from the first tree to another node in the second tree.

    **Note** that queries are independent from each other. That is, for every query you
    will remove the added edge before proceeding to the next query."""

    def max_target_nodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        # Helper function to build adjacency list
        def build_adj(edges, n):
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        # Helper function to perform BFS and compute even/odd counts and levels
        def bfs_count(tree, root):
            n = len(tree)
            level = [-1] * n
            level[root] = 0
            q = deque([root])
            even_count = 0
            odd_count = 0
            while q:
                u = q.popleft()
                if level[u] % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                for v in tree[u]:
                    if level[v] == -1:
                        level[v] = level[u] + 1
                        q.append(v)
            return even_count, odd_count, level

        # Compute sizes of the trees
        n = len(edges1) + 1  # Number of nodes in first tree
        m = len(edges2) + 1  # Number of nodes in second tree

        # Build adjacency lists
        adj1 = build_adj(edges1, n)
        adj2 = build_adj(edges2, m)

        # BFS on second tree to get the size of the larger color class
        even_count2, odd_count2, _ = bfs_count(adj2, 0)
        max_size = max(even_count2, odd_count2)

        # BFS on first tree to get level parities and counts
        count0, count1, level = bfs_count(adj1, 0)

        # Compute answer for each node i in the first tree
        answer = [0] * n
        for i in range(n):
            if level[i] % 2 == 0:
                answer[i] = count0 + max_size
            else:
                answer[i] = count1 + max_size

        return answer

    maxTargetNodes = max_target_nodes
