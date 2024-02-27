# https://leetcode.com/problems/same-tree/


class Solution:
    """100. Same Tree

    Given the roots of two binary trees `p` and `q`, write a function to check if they
    are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the
    nodes have the same value.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both trees are None, they are the same
        if not p and not q:
            return True
        # If one of the trees is None and the other is not, they are not the same
        elif not p or not q:
            return False
        # Check if current nodes have the same value and recursively check their left and right subtrees
        else:
            return (
                p.val == q.val
                and self.is_same_tree(p.left, q.left)
                and self.is_same_tree(p.right, q.right)
            )

    isSameTree = is_same_tree
