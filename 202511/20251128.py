# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
import sys
from typing import List

sys.setrecursionlimit(10**5)

class Solution:
    """2872. Maximum Number of K-Divisible Components

    There is an undirected tree with n nodes labeled from 0 to n - 1.
    You are given the integer n and a 2D integer array edges of length
    n - 1, where edges[i] = [ai, bi] indicates that there is an edge
    between nodes ai and bi in the tree.

    You are also given a 0-indexed integer array values of length n,
    where values[i] is the value associated with the ith node, and an
    integer k.

    A valid split of the tree is obtained by removing any set of edges,
    possibly empty, from the tree such that the resulting components all
    have values that are divisible by k, where the value of a connected
    component is the sum of the values of its nodes.

    Return the maximum number of components in any valid split.
    """
    def max_k_divisible_components(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build adjacency list for the tree
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(u: int, p: int) -> tuple[int, int]:
            # Initialize mod sum with current node's value % k
            mod_sum = values[u] % k
            # Initialize split-off components count
            split_comp = 0
            for v in adj[u]:
                if v != p:
                    # Recurse on child
                    child_mod, child_split = dfs(v, u)
                    # Accumulate mod sum
                    mod_sum = (mod_sum + child_mod) % k
                    # Add child's split components
                    split_comp += child_split
                    # If child's subtree sum % k == 0, detach it for +1 component
                    if child_mod == 0:
                        split_comp += 1
            return mod_sum, split_comp
        
        # Run DFS from root 0
        _, max_split = dfs(0, -1)
        # Total components = split-offs + 1 (root remaining, valid since total % k == 0)
        return max_split + 1

    maxKDivisibleComponents = max_k_divisible_components