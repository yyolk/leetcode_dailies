# https://leetcode.com/problems/leaf-similar-trees/


class Solution:
    """872. Leaf-Similar Trees

    Consider all the leaves of a binary tree, from left to right order, the values of
    those leaves form a **leaf value sequence***.*

    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

    For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

    Two binary trees are considered *leaf-similar* if their leaf value sequence is the
    same.

    Return `true` if and only if the two given trees with head nodes `root1` and `root2`
    are leaf-similar.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def leaf_similar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def get_leaf_values(root, values):
            """Helper function to get the leaf values of a binary tree."""
            if not root:
                return
            # Check if the node is a leaf (has no left or right children)
            if not root.left and not root.right:
                values.append(root.val)  # Append the leaf value to the list
            # Recursively traverse the left and right subtrees
            get_leaf_values(root.left, values)
            get_leaf_values(root.right, values)

        # Initialize lists to store leaf values of each tree
        leaf_values1 = []
        leaf_values2 = []

        # Populate the lists with leaf values for both trees
        get_leaf_values(root1, leaf_values1)
        get_leaf_values(root2, leaf_values2)

        # Check if the leaf value sequences of the two trees are the same
        return leaf_values1 == leaf_values2

    leafSimilar = leaf_similar
