# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


class Solution:
    """889. Construct Binary Tree from Preorder and Postorder Traversal

    Given two integer arrays, `preorder` and `postorder` where `preorder` is the
    preorder traversal of a binary tree of **distinct** values and `postorder` is the
    postorder traversal of the same tree, reconstruct and return *the binary tree*.

    If there exist multiple answers, you can **return any** of them."""

    def construct_from_pre_post(
        self, preorder: list[int], postorder: list[int]
    ) -> Optional[TreeNode]: ...

    constructFromPrePost = construct_from_pre_post
