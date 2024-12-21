# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
from collections import defaultdict


class Solution:
    """2872. Maximum Number of K-Divisible Components

    There is an undirected tree with `n` nodes labeled from `0` to `n - 1`. You are
    given the integer `n` and a 2D integer array `edges` of length `n - 1`, where
    `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in
    the tree.

    You are also given a **0-indexed** integer array `values` of length `n`, where
    `values[i]` is the **value** associated with the `ith` node, and an integer `k`.

    A **valid split** of the tree is obtained by removing any set of edges, possibly
    empty, from the tree such that the resulting components all have values that are
    divisible by `k`, where the **value of a connected component** is the sum of the
    values of its nodes.

    Return *the **maximum number of components** in any valid split*."""

    def max_k_divisible_components(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:

        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # Visited set to track visited nodes
        visited = set()

        # Variable to count the number of components
        components = 0

        def dfs(node: int) -> int:
            """Perform DFS and calculate subtree sums."""
            nonlocal components

            visited.add(node)
            # Start with the value of the current node
            subtree_sum = values[node]

            for neighbor in tree[node]:
                if neighbor not in visited:
                    # Recursively calculate the sum for the subtree
                    child_sum = dfs(neighbor)
                    subtree_sum += child_sum

            # If the subtree sum is divisible by k, it forms a component
            if subtree_sum % k == 0:
                components += 1
                return 0  # Reset the sum for this subtree

            return subtree_sum

        # Start DFS from node 0 (or any arbitrary node)
        dfs(0)

        return components

    maxKDivisibleComponents = max_k_divisible_components
