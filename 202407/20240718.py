# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/


class Solution:
    """1530. Number of Good Leaf Nodes Pairs

    You are given the `root` of a binary tree and an integer `distance`. A pair of two
    different **leaf** nodes of a binary tree is said to be good if the length of **the
    shortest path** between them is less than or equal to `distance`.

    Return *the number of good leaf node pairs* in the tree.

    """

    def count_pairs(self, root: TreeNode, distance: int) -> int: ...

    countPairs = count_pairs
