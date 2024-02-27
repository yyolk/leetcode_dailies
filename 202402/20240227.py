# https://leetcode.com/problems/diameter-of-binary-tree/


class Solution:
    """543. Diameter of Binary Tree

    Given the `root` of a binary tree, return *the length of the **diameter** of the
    tree*.

    The **diameter** of a binary tree is the **length** of the longest path between any
    two nodes in a tree. This path may or may not pass through the `root`.

    The **length** of a path between two nodes is represented by the number of edges
    between them.

    Definition for a binary tree node.

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        # Initialize the variable to store the maximum diameter
        diameter = 0

        # Helper function for DFS traversal and diameter calculation
        def dfs(node):
            # Access the outer 'diameter' variable
            nonlocal diameter

            # Base case: If the node is None, return 0
            if not node:
                return 0

            # Recursively calculate the height of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the diameter with the maximum diameter encountered so far
            diameter = max(diameter, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        # Start DFS traversal from the root
        dfs(root)

        # Return the final result representing the diameter of the binary tree
        return diameter

    diameterOfBinaryTree = diameter_of_binary_tree
