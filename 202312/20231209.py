# https://leetcode.com/problems/binary-tree-inorder-traversal/


class Solution:
    """94. Binary Tree Inorder Traversal

    Given the `root` of a binary tree, return *the inorder traversal of its nodes'
    values*.

    Definition for a binary tree node.

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def inorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        """Get the inorder traversal of an input binary tree.

        Args:
            root: The input binary tree.

        Returns:
            The inorder traversal of the input its nodes' values.
        """
        result: list[int] = []

        def inorder_recursive(node: Optional[TreeNode]):
            """Helper inner recursive function for traversal."""
            nonlocal result
            if node:
                inorder_recursive(node.left)
                result.append(node.val)
                inorder_recursive(node.right)

        inorder_recursive(root)
        return result

    inorderTraversal = inorder_traversal
