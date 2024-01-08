# https://leetcode.com/problems/range-sum-of-bst/


class Solution:
    """938. Range Sum of BST

    Given the `root` node of a binary search tree and two integers `low` and `high`,
    return *the sum of values of all nodes with a value in the **inclusive** range*
    `[low, high]`.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def range_sum_b_s_t(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Initialize the result to store the sum
        result = 0

        def dfs(node):
            """Helper function for DFS traversal."""
            nonlocal result
            if node:
                # Check if the node value is within the specified range
                if low <= node.val <= high:
                    result += node.val
                # If the node value is greater than the low limit, explore the left subtree
                if node.val > low:
                    dfs(node.left)
                # If the node value is less than the high limit, explore the right subtree
                if node.val < high:
                    dfs(node.right)

        # Start DFS traversal from the root
        dfs(root)
        return result

    rangeSumBST = range_sum_b_s_t
