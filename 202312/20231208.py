# https://leetcode.com/problems/construct-string-from-binary-tree/


class Solution:
    """606. Construct String from Binary Tree

    Given the `root` of a binary tree, construct a string consisting of parenthesis and
    integers from a binary tree with the preorder traversal way, and return it.

    Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
    relationship between the string and the original binary tree.

    Definition for a binary tree node.

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def tree2str(self, root: Optional[TreeNode]) -> str:
        """Constructs a string representation of the input binary tree.

        Args:
            root: The input binary tree.

        Returns:
            The constructed string consisting of parenthses and integers from a binary
                tree with the preorder traversal way. With empty parenthesis omitted
                when they do not affect the one-to-one mapping relationship.
        """

        def preorder(node: Optional[TreeNode]) -> str:
            """Helper function for preorder traversal."""
            if not node:
                return ""

            # Add the value of the current node.
            result = str(node.val)

            # Recursively process left and right subtree.
            left_str = preorder(node.left)
            right_str = preorder(node.right)

            # Include left subtree if either left subtree or right subtree exists.
            if node.left or node.right:
                result += "(" + left_str + ")"

            # Include right subtree only if it exists.
            if node.right:
                result += "(" + right_str + ")"

            return result

        return preorder(root)
