# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


class Solution:
    """1038. Binary Search Tree to Greater Sum Tree

    Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such
    that every key of the original BST is changed to the original key plus the sum of
    all keys greater than the original key in BST.

    As a reminder, a *binary search tree* is a tree that satisfies these constraints:

    * The left subtree of a node contains only nodes with keys **less than** the node's
    key.

    * The right subtree of a node contains only nodes with keys **greater than** the
    node's key.

    * Both the left and right subtrees must also be binary search trees.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        # Initialize the running sum to 0
        self.sum = 0

        def reverse_inorder(node):
            # Base case: if the node is None, return
            if not node:
                return
            # Recursively call on the right subtree
            reverse_inorder(node.right)
            # Update the running sum with the current node's value
            self.sum += node.val
            # Update the current node's value to the running sum
            node.val = self.sum
            # Recursively call on the left subtree
            reverse_inorder(node.left)

        # Start the reverse in-order traversal from the root
        reverse_inorder(root)
        return root

    bstToGst = bst_to_gst
