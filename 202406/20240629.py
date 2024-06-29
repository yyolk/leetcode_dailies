# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/


class Solution:
    """2192. All Ancestors of a Node in a Directed Acyclic Graph

    You are given a positive integer `n` representing the number of nodes of a
    **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to `n - 1`
    (**inclusive**).

    You are also given a 2D integer array `edges`, where `edges[i] = [fromi, toi]`
    denotes that there is a **unidirectional** edge from `fromi` to `toi` in the graph.

    Return *a list* `answer`*, where* `answer[i]` *is the **list of ancestors** of the*
    `ith` *node, sorted in **ascending order***.

    A node `u` is an **ancestor** of another node `v` if `u` can reach `v` via a set of
    edges.

    """


    def dfs(self, x: int, curr: int, ans: list[list[int]], directChild: list[list[int]]) -> None:
        # Traverse all direct children of the current node
        for ch in directChild[curr]:
            # If the ancestor list of the child node is empty or doesn't end with the current ancestor
            if not ans[ch] or ans[ch][-1] != x:
                # Append the current ancestor to the child's ancestor list
                ans[ch].append(x)
                # Recursively perform DFS on the child node
                self.dfs(x, ch, ans, directChild)

    def get_ancestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Initialize the ancestor lists for all nodes
        ans = [[] for _ in range(n)]
        # Initialize the adjacency list for all nodes
        directChild = [[] for _ in range(n)]
        # Build the adjacency list from the given edges
        for e in edges:
            directChild[e[0]].append(e[1])
        # Perform DFS for each node to find all ancestors
        for i in range(n):
            self.dfs(i, i, ans, directChild)
        # Return the list of ancestors for each node
        return ans

    getAncestors = get_ancestors
