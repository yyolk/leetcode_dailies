# https://leetcode.com/problems/flip-equivalent-binary-trees/


class Solution:
    """951. Flip Equivalent Binary Trees

    For a binary tree **T**, we can define a **flip operation** as follows: choose any
    node, and swap the left and right child subtrees.

    A binary tree **X** is *flip equivalent* to a binary tree **Y** if and only if we
    can make **X** equal to **Y** after some number of flip operations.

    Given the roots of two binary trees `root1` and `root2`, return `true` if the two
    trees are flip equivalent or `false` otherwise.

    """

    def flip_equiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool: ...

    flipEquiv = flip_equiv
