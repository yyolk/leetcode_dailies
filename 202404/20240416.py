# https://leetcode.com/problems/add-one-row-to-tree/
from typing import Optional


class Solution:
    """623. Add One Row to Tree

    Given the `root` of a binary tree and two integers `val` and `depth`, add a row of
    nodes with value `val` at the given depth `depth`.

    Note that the `root` node is at depth `1`.

    The adding rule is:

    * Given the integer `depth`, for each not null tree node `cur` at the depth `depth -
    1`, create two tree nodes with value `val` as `cur`'s left subtree root and right
    subtree root.

    * `cur`'s original left subtree should be the left subtree of the new left subtree
    root.

    * `cur`'s original right subtree should be the right subtree of the new right
    subtree root.

    * If `depth == 1` that means there is no depth `depth - 1` at all, then create a
    tree node with value `val` as the new root of the whole original tree, and the
    original tree is the new root's left subtree.

    Definition for a binary tree node::

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def add_one_row(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        # If depth is 1, create a new root with the original tree as its left subtree
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        # Call the helper function to recursively add the row at the specified depth
        self._add_row(root, val, depth)
        return root

    def _add_row(self, node, val, depth):
        # Base case: if the current node is None or the depth is 1, return
        if not node:
            return
        # If depth is 2, create new nodes for the left and right subtrees
        if depth == 2:
            left_node = TreeNode(val)
            right_node = TreeNode(val)
            left_node.left = node.left
            right_node.right = node.right
            node.left = left_node
            node.right = right_node
        else:
            # Recursively call the function for left and right subtrees
            self._add_row(node.left, val, depth - 1)
            self._add_row(node.right, val, depth - 1)

    addOneRow = add_one_row
