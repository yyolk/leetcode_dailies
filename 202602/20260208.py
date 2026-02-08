# https://leetcode.com/problems/balanced-binary-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """110. Balanced Binary Tree
    
    Given a binary tree, determine if it is height-balanced.
    
    A height-balanced binary tree is a binary tree in which the depth of the
    two subtrees of every node never differs by more than one.
    """
    def is_balanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> int:
            # Base case: empty subtree has height 0
            if not node:
                return 0
            
            # Compute left subtree height; -1 means unbalanced
            left = dfs(node.left)
            if left == -1:
                return -1
            
            # Compute right subtree height; -1 means unbalanced
            right = dfs(node.right)
            if right == -1:
                return -1
            
            # If current node subtrees differ by >1, mark unbalanced
            if abs(left - right) > 1:
                return -1
            
            # Return actual height of current subtree
            return max(left, right) + 1
        
        # Tree is balanced if root dfs returns non-negative height
        return dfs(root) != -1

    isBalanced = is_balanced