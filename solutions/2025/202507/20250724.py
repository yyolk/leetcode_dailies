# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/


class Solution:
    """2322. Minimum Score After Removals on a Tree

    There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and
    `n - 1` edges.

    You are given a **0-indexed** integer array `nums` of length `n` where `nums[i]`
    represents the value of the `ith` node. You are also given a 2D integer array
    `edges` of length `n - 1` where `edges[i] = [ai, bi]` indicates that there is an
    edge between nodes `ai` and `bi` in the tree.

    Remove two **distinct** edges of the tree to form three connected components. For a
    pair of removed edges, the following steps are defined:

    1. Get the XOR of all the values of the nodes for **each** of the three components
    respectively.

    2. The **difference** between the **largest** XOR value and the **smallest** XOR
    value is the **score** of the pair.

    * For example, say the three components have the node values: `[4,5,7]`, `[1,9]`,
    and `[3,3,3]`. The three XOR values are `4 ^ 5 ^ 7 = 6`, `1 ^ 9 = 8`, and `3 ^ 3 ^ 3
    = 3`. The largest XOR value is `8` and the smallest XOR value is `3`. The score is
    then `8 - 3 = 5`.

    Return *the **minimum** score of any possible pair of edge removals on the given
    tree*."""

    def minimum_score(self, nums: list[int], edges: list[list[int]]) -> int:
        # Get the number of nodes
        n = len(nums)
        # Handle edge case where tree has fewer than 3 nodes
        if n < 3:
            return 0
        # Initialize adjacency list for the tree
        adj = [[] for _ in range(n)]
        # Build adjacency list from edges
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        # Initialize array to store XOR of each subtree
        subtree_xor = [0] * n
        # Initialize arrays to track DFS entry and exit times
        enter = [0] * n
        exit_ = [0] * n
        # Initialize timer for DFS traversal
        timer = 0

        # Define DFS function to compute subtree XOR and entry/exit times
        def dfs(node, parent):
            nonlocal timer
            # Record entry time for current node
            enter[node] = timer
            # Increment timer
            timer += 1
            # Initialize subtree XOR with current node's value
            subtree_xor[node] = nums[node]
            # Process all neighbors except parent
            for nei in adj[node]:
                if nei != parent:
                    # Recursively process child node
                    dfs(nei, node)
                    # Update subtree XOR with child's XOR
                    subtree_xor[node] ^= subtree_xor[nei]
            # Record exit time for current node
            exit_[node] = timer

        # Start DFS from root (node 0)
        dfs(0, -1)
        # Compute total XOR of all nodes
        total = subtree_xor[0]
        # Initialize minimum score to maximum possible integer
        import sys

        min_score = sys.maxsize
        # Iterate over all pairs of nodes to consider edge removals
        for u in range(1, n):
            for v in range(1, n):
                # Skip if same node
                if u == v:
                    continue
                # Case 1: Node v is in subtree of u
                if enter[u] <= enter[v] < exit_[u]:
                    # XOR of component containing v
                    xor1 = subtree_xor[v]
                    # XOR of component containing u but not v
                    xor2 = subtree_xor[u] ^ xor1
                    # XOR of remaining nodes
                    xor3 = total ^ subtree_xor[u]
                # Case 2: Node u is in subtree of v
                elif enter[v] <= enter[u] < exit_[v]:
                    # XOR of component containing u
                    xor1 = subtree_xor[u]
                    # XOR of component containing v but not u
                    xor2 = subtree_xor[v] ^ xor1
                    # XOR of remaining nodes
                    xor3 = total ^ subtree_xor[v]
                # Case 3: Nodes u and v are in different subtrees
                else:
                    # XOR of component containing u
                    xor1 = subtree_xor[u]
                    # XOR of component containing v
                    xor2 = subtree_xor[v]
                    # XOR of remaining nodes
                    xor3 = total ^ xor1 ^ xor2
                # Compute maximum XOR value
                current_max = max(xor1, xor2, xor3)
                # Compute minimum XOR value
                current_min = min(xor1, xor2, xor3)
                # Update minimum score if current score is smaller
                min_score = min(min_score, current_max - current_min)
        # Return the minimum score found
        return min_score

    minimumScore = minimum_score
