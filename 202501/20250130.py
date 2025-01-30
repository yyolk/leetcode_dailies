# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/


class Solution:
    """2493. Divide Nodes Into the Maximum Number of Groups

    You are given a positive integer `n` representing the number of nodes in an
    **undirected** graph. The nodes are labeled from `1` to `n`.

    You are also given a 2D integer array `edges`, where `edges[i] = [ai, bi]` indicates
    that there is a **bidirectional** edge between nodes `ai` and `bi`. **Notice** that
    the given graph may be disconnected.

    Divide the nodes of the graph into `m` groups (**1-indexed**) such that:

    * Each node in the graph belongs to exactly one group.

    * For every pair of nodes in the graph that are connected by an edge `[ai, bi]`, if
    `ai` belongs to the group with index `x`, and `bi` belongs to the group with index
    `y`, then `|y - x| = 1`.

    Return *the maximum number of groups (i.e., maximum* `m`*) into which you can divide
    the nodes*. Return `-1` *if it is impossible to group the nodes with the given
    conditions*."""

    def magnificent_sets(self, n: int, edges: list[list[int]]) -> int: ...

    magnificentSets = magnificent_sets
