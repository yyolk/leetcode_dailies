# https://leetcode.com/problems/even-odd-tree/
from collections import deque
from typing import Optional


class Solution:
    """1609. Even Odd Tree

    A binary tree is named **Even-Odd** if it meets the following conditions:

    * The root of the binary tree is at level index `0`, its children are at level index
    `1`, their children are at level index `2`, etc.

    * For every **even-indexed** level, all nodes at the level have **odd** integer
    values in **strictly increasing** order (from left to right).

    * For every **odd-indexed** level, all nodes at the level have **even** integer
    values in **strictly decreasing** order (from left to right).

    Given the `root` of a binary tree, *return* `true` *if the binary tree is **Even-
    Odd**, otherwise return* `false`*.*

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def is_even_odd_tree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_value = (
                None  # To track the previous node's value within the current level
            )

            for _ in range(level_size):
                node = queue.popleft()

                # Check the validity of the current node's value based on the level
                if (
                    level % 2 == 0
                    and (
                        node.val % 2 == 0
                        or (prev_value is not None and node.val <= prev_value)
                    )
                ) or (
                    level % 2 == 1
                    and (
                        node.val % 2 == 1
                        or (prev_value is not None and node.val >= prev_value)
                    )
                ):
                    return False

                # Update the previous value for the next iteration
                prev_value = node.val

                # Add the children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Move to the next level
            level += 1

        return True

    isEvenOddTree = is_even_odd_tree
