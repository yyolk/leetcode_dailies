# https://leetcode.com/problems/binary-tree-postorder-traversal/


class Solution:
    """145. Binary Tree Postorder Traversal

    Given the `root` of a binary tree, return *the postorder traversal of its nodes'
    values*.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def postorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        # Initialize an empty list to store the result of the traversal.
        result = []
        
        # Define a helper function to perform the recursive postorder traversal.
        def traverse(node: Optional[TreeNode]):
            if node:
                # First, recursively traverse the left subtree.
                traverse(node.left)
                # Then, recursively traverse the right subtree.
                traverse(node.right)
                # Finally, visit the current node by adding its value to the result list.
                result.append(node.val)
        
        # Start the traversal from the root of the tree.
        traverse(root)
        
        # Return the result list containing the postorder traversal.
        return result

    postorderTraversal = postorder_traversal
