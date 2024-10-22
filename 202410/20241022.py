# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/


class Solution:
    """2583. Kth Largest Sum in a Binary Tree

    You are given the `root` of a binary tree and a positive integer `k`.

    The **level sum** in the tree is the sum of the values of the nodes that are on the
    **same** level.

    Return *the* `kth` ***largest** level sum in the tree (not necessarily distinct)*.
    If there are fewer than `k` levels in the tree, return `-1`.

    **Note** that two nodes are on the same level if they have the same distance from
    the root.

    """

    def kth_largest_level_sum(self, root: Optional[TreeNode], k: int) -> int: ...

    kthLargestLevelSum = kth_largest_level_sum
