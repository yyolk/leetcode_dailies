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

    def get_ancestors(self, n: int, edges: list[list[int]]) -> list[list[int]]: ...

    getAncestors = get_ancestors
