# https://leetcode.com/problems/find-largest-value-in-each-tree-row/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """515. Find Largest Value in Each Tree Row

    Given the `root` of a binary tree, return *an array of the largest value in each
    row* of the tree **(0-indexed)**.
    """

    def largest_values(self, root: Optional[TreeNode]) -> list[int]:
        """Returns an array of the largest value in each row of the tree.

        Proposed solution using Breadth-First-Search (BFS).

        Args:
            root (Optional TreeNode): The input binary TreeNode.
        Returns:
            list of int: The largest value of each row in the tree.
        """
        if not root:
            return []

        # Our list to store the largest values of each row
        result = []
        # Initialize a queue for BFS, starting with the root node
        queue = [root]

        while queue:
            # Initialize the maximum value for the current level -1 than the constraint
            level_max = -(2**31) - 1
            # Get the number of nodes in the current level
            level_size = len(queue)

            for _ in range(level_size):
                # Dequeue the first node in the current level
                node = queue.pop(0)
                # Update the maximum value for the current level
                level_max = max(level_max, node.val)

                if node.left:
                    # Enqueue the left child, if it exists
                    queue.append(node.left)
                if node.right:
                    # Enqueue the right child, if it exists
                    queue.append(node.right)

            # Append the maximum value for the current level to the result list
            result.append(level_max)

        # Return the result list of the final results
        return result

    largestValues = largest_values
