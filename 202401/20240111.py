# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/


class Solution:
    """1026. Maximum Difference Between Node and Ancestor

    Given the `root` of a binary tree, find the maximum value `v` for which there exist
    **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor
    of `b`.

    A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any
    child of `a` is an ancestor of `b`.
    """

    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        ...

    maxAncestorDiff = max_ancestor_diff
