# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/


class Solution:
    """3203. Find Minimum Diameter After Merging Two Trees

    There exist two **undirected** trees with `n` and `m` nodes, numbered from `0` to `n
    - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays
    `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i]
    = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the first
    tree and `edges2[i] = [ui, vi]` indicates that there is an edge between nodes `ui`
    and `vi` in the second tree.

    You must connect one node from the first tree with another node from the second tree
    with an edge.

    Return the **minimum** possible **diameter** of the resulting tree.

    The **diameter** of a tree is the length of the *longest* path between any two nodes
    in the tree."""

    def minimum_diameter_after_merge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int: ...

    minimumDiameterAfterMerge = minimum_diameter_after_merge
