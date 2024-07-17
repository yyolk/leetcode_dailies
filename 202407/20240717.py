# https://leetcode.com/problems/delete-nodes-and-return-forest/
from typing import Optional


class Solution:
    """1110. Delete Nodes And Return Forest

    Given the `root` of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in `to_delete`, we are left with a forest (a
    disjoint union of trees).

    Return the roots of the trees in the remaining forest. You may return the result in
    any order.

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def del_nodes(
        self, root: Optional[TreeNode], to_delete: list[int]
    ) -> list[TreeNode]:
        to_delete_set = set(to_delete)  # Convert list to set for O(1) lookups
        forest = []

        def helper(node, is_root):
            if not node:
                return None

            # Determine if the current node needs to be deleted
            node_deleted = node.val in to_delete_set

            # If the node is a root and is not deleted, add it to the forest
            if is_root and not node_deleted:
                forest.append(node)

            # Recursively process the left and right children
            node.left = helper(node.left, node_deleted)
            node.right = helper(node.right, node_deleted)

            # Return None if the current node is deleted, otherwise return the node itself
            return None if node_deleted else node

        helper(root, True)
        return forest

    delNodes = del_nodes
