# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/


class Solution:
    """1026. Maximum Difference Between Node and Ancestor

    Given the `root` of a binary tree, find the maximum value `v` for which there exist
    **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor
    of `b`.

    A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any
    child of `a` is an ancestor of `b`.

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_val, max_val):
            # Base case: if the node is None, return the difference between max and min
            if not node:
                return max_val - min_val

            # Update min and max values encountered so far
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            # Recursively calculate the maximum ancestor difference for left and right subtrees
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)

            # Return the maximum difference between left and right subtrees
            return max(left_diff, right_diff)

        # Start DFS from the root with initial min and max values set to root's value
        return dfs(root, root.val, root.val)

    maxAncestorDiff = max_ancestor_diff
