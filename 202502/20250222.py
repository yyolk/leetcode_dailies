# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
import re


# class TreeNode:
#     """Definition of a TreeNode."""
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """1028. Recover a Tree From Preorder Traversal

    We run a preorder depth-first search (DFS) on the `root` of a binary tree.

    At each node in this traversal, we output `D` dashes (where `D` is the depth of this
    node), then we output the value of this node.  If the depth of a node is `D`, the
    depth of its immediate child is `D + 1`.  The depth of the `root` node is `0`.

    If a node has only one child, that child is guaranteed to be **the left child**.

    Given the output `traversal` of this traversal, recover the tree and return *its*
    `root`."""

    def recover_from_preorder(self, traversal: str) -> TreeNode | None:
        # Parse the traversal string to get list of (depth, value)
        nodes = []
        for match in re.finditer(r"(-*)(\d+)", traversal):
            depth = len(match.group(1))
            value = int(match.group(2))
            nodes.append((depth, value))

        if not nodes:
            return None

        # Initialize stack and root
        stack = []
        root = None

        for depth, value in nodes:
            new_node = TreeNode(value)
            # Pop stack until it has 'depth' number of nodes
            while len(stack) > depth:
                stack.pop()
            if len(stack) == 0:
                root = new_node
            else:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = new_node
                else:
                    parent.right = new_node
            stack.append(new_node)

        return root

    recoverFromPreorder = recover_from_preorder
