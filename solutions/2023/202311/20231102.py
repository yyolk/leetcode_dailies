# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/


class Solution:
    """2265. Count Nodes Equal to Average of Subtree

    Given the `root` of a binary tree, return *the number of nodes where the value of
    the node is equal to the **average** of the values in its **subtree***.

    Note:

    * The **average** of `n` elements is the **sum** of the `n` elements divided by `n`
    and **rounded down** to the nearest integer.

    * A **subtree** of `root` is a tree consisting of `root` and all of its descendants.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def average_of_subtree(self, root: TreeNode | None) -> int:
        """
        Counts the number of nodes in the binary tree where the value of the node is equal
        to the average of the values in its subtree.

        Args:
            root: The root of the binary tree.

        Returns:
            The number of nodes with values equal to the average of their subtrees.

        Note:
        - The average of `n` elements is the sum of the `n` elements divided by `n` and
            rounded down to the nearest integer.
        - A subtree of `root` is a tree consisting of `root` and all of its descendants.
        """
        result = 0

        def traverse(node: TreeNode | None) -> (int, int):
            """
            Helper function for depth-first search to calculate subtree averages.

            Args:
                node: The current node in the binary tree.

            Returns:
                A tuple containing the total value and the total number of nodes in the
                    subtree.
            """
            nonlocal result

            if not node:
                # (total value, total nodes)
                return 0, 0

            left_total, left_count = traverse(node.left)
            right_total, right_count = traverse(node.right)

            total = node.val + left_total + right_total
            count = 1 + left_count + right_count

            if total // count == node.val:
                result += 1

            return total, count

        traverse(root)
        return result

    averageOfSubtree = average_of_subtree
