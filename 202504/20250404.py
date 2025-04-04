# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


class Solution:
    """1123. Lowest Common Ancestor of Deepest Leaves

    Given the `root` of a binary tree, return *the lowest common ancestor of its deepest
    leaves*.

    Recall that:

    * The node of a binary tree is a leaf if and only if it has no children

    * The depth of the root of the tree is `0`. if the depth of a node is `d`, the depth
    of each of its children is `d + 1`.

    * The lowest common ancestor of a set `S` of nodes, is the node `A` with the largest
    depth such that every node in `S` is in the subtree with root `A`."""

    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]: ...

    lcaDeepestLeaves = lca_deepest_leaves
