# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/


class Solution:
    """3372. Maximize the Number of Target Nodes After Connecting Trees I

    There exist two **undirected** trees with `n` and `m` nodes, with **distinct**
    labels in ranges `[0, n - 1]` and `[0, m - 1]`, respectively.

    You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m
    - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge
    between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates
    that there is an edge between nodes `ui` and `vi` in the second tree. You are also
    given an integer `k`.

    Node `u` is **target** to node `v` if the number of edges on the path from `u` to
    `v` is less than or equal to `k`. **Note** that a node is *always* **target** to
    itself.

    Return an array of `n` integers `answer`, where `answer[i]` is the **maximum**
    possible number of nodes **target** to node `i` of the first tree if you have to
    connect one node from the first tree to another node in the second tree.

    **Note** that queries are independent from each other. That is, for every query you
    will remove the added edge before proceeding to the next query."""

    def max_target_nodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]: ...

    maxTargetNodes = max_target_nodes
