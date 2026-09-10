# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """2265. Count Nodes Equal to Average of Subtree

    Given the `root` of a binary tree, return *the number of nodes where the
    value of the node is equal to the **average** of the values in its
    **subtree***.

    **Note:**

    * The **average** of `n` elements is the **sum** of the `n` elements
    divided by `n` and **rounded down** to the nearest integer.

    * A **subtree** of `root` is a tree consisting of `root` and all of its
    descendants.

    Constraints:

    * The number of nodes in the tree is in the range `[1, 1000]`.

    * `0 <= Node.val <= 1000`

    Definition for a binary tree node.

        class TreeNode:

        def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right
    """

    def average_of_subtree(self, root: TreeNode) -> int:
        # Post-order DFS: return (subtree_sum, subtree_node_count)
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total = node.val + left_sum + right_sum
            count = 1 + left_count + right_count
            # Integer division matches the problem's floor-average rule
            if total // count == node.val:
                nonlocal ans
                ans += 1
            return total, count

        ans = 0
        dfs(root)
        return ans

    averageOfSubtree = average_of_subtree
