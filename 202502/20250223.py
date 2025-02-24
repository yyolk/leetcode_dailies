# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


# class TreeNode:
#     """Definition for a binary tree node."""
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """889. Construct Binary Tree from Preorder and Postorder Traversal

    Given two integer arrays, `preorder` and `postorder` where `preorder` is the
    preorder traversal of a binary tree of **distinct** values and `postorder` is the
    postorder traversal of the same tree, reconstruct and return *the binary tree*.

    If there exist multiple answers, you can **return any** of them."""

    def construct_from_pre_post(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        if not preorder or not postorder:
            return None

        # Create a hash map for postorder values to quickly find indices
        post_map = {val: idx for idx, val in enumerate(postorder)}

        def build(
            pre_start: int, pre_end: int, post_start: int, post_end: int
        ) -> TreeNode | None:
            # Base case: if no elements to process
            if pre_start > pre_end:
                return None

            # Create root node from the first element of preorder
            root = TreeNode(preorder[pre_start])

            # If only one element, return the root
            if pre_start == pre_end:
                return root

            # The next element in preorder will be the left child
            left_val = preorder[pre_start + 1]
            # Find where left subtree ends in postorder
            left_post_end = post_map[left_val]

            # Calculate size of left subtree
            left_size = left_post_end - post_start + 1

            # Recursively build left and right subtrees
            root.left = build(
                pre_start + 1,  # Start of left in preorder
                pre_start + left_size,  # End of left in preorder
                post_start,  # Start of left in postorder
                left_post_end,  # End of left in postorder
            )

            root.right = build(
                pre_start + left_size + 1,  # Start of right in preorder
                pre_end,  # End of right in preorder
                left_post_end + 1,  # Start of right in postorder
                post_end - 1,  # End of right in postorder (exclude root)
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)

    constructFromPrePost = construct_from_pre_post
