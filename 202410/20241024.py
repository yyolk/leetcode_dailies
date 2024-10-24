# https://leetcode.com/problems/flip-equivalent-binary-trees/


class Solution:
    """951. Flip Equivalent Binary Trees

    For a binary tree **T**, we can define a **flip operation** as follows: choose any
    node, and swap the left and right child subtrees.

    A binary tree **X** is *flip equivalent* to a binary tree **Y** if and only if we
    can make **X** equal to **Y** after some number of flip operations.

    Given the roots of two binary trees `root1` and `root2`, return `true` if the two
    trees are flip equivalent or `false` otherwise.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def flip_equiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None, trees are equivalent
        if not root1 and not root2:
            return True

        # If one node is None and the other isn't, or if their values differ, they're not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # Check if the trees are equivalent with or without flipping
        # Here we check two scenarios:
        # 1. Without flipping: left with left, right with right
        # 2. With flipping: left with right, right with left
        return (
            self.flip_equiv(root1.left, root2.left)
            and self.flip_equiv(root1.right, root2.right)
        ) or (
            self.flip_equiv(root1.left, root2.right)
            and self.flip_equiv(root1.right, root2.left)
        )

    flipEquiv = flip_equiv
