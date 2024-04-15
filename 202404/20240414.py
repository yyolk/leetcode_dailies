# https://leetcode.com/problems/sum-of-left-leaves/
from typing import Optional


class Solution:
    """404. Sum of Left Leaves

    Given the `root` of a binary tree, return *the sum of all left leaves.*

    A **leaf** is a node with no children. A **left leaf** is a leaf that is the left
    child of another node.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def sum_of_left_leaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def is_leaf(node):
            return node and not node.left and not node.right

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left) if node.left else 0
            right_sum = dfs(node.right) if node.right else 0

            if is_leaf(node.left):
                return node.left.val + right_sum
            else:
                return left_sum + right_sum

        return dfs(root)

    sumOfLeftLeaves = sum_of_left_leaves
