# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def lca_deepest_leaves(self, root: TreeNode | None) -> TreeNode | None:
        def helper(node: TreeNode | None, depth: int) -> tuple[int, TreeNode | None]:
            # Base case: null node
            if not node:
                return (-1, None)
            # Base case: leaf node
            if not node.left and not node.right:
                return (depth, node)
            # Recurse on left and right children
            left_max_depth, left_lca = helper(node.left, depth + 1)
            right_max_depth, right_lca = helper(node.right, depth + 1)
            # Compare depths to determine LCA
            if left_max_depth > right_max_depth:
                return (left_max_depth, left_lca)
            elif right_max_depth > left_max_depth:
                return (right_max_depth, right_lca)
            else:
                return (left_max_depth, node)
        
        # Start recursion from root at depth 0 and return the LCA
        return helper(root, 0)[1]

    lcaDeepestLeaves = lca_deepest_leaves
