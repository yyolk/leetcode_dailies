# https://leetcode.com/problems/cousins-in-binary-tree-ii/
from collections import deque, defaultdict
from typing import Optional


class Solution:
    """2641. Cousins in Binary Tree II

    Given the `root` of a binary tree, replace the value of each node in the tree with
    the **sum of all its cousins' values**.

    Two nodes of a binary tree are **cousins** if they have the same depth with
    different parents.

    Return *the* `root` *of the modified tree*.

    **Note** that the depth of a node is the number of edges in the path from the root
    node to it.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """
    def __init__(self):
        # Initialize the level sum table
        self.level_sum_table = defaultdict(int)

    def depth_first_search_update(self, current_node: Optional["TreeNode"]):
        # If the current node does not exist, return immediately
        if not current_node:
            return

        # For the root node, set value to 0 as it has no cousins
        # For other nodes, set the value to the sum of all nodes at this level minus the sum of its siblings
        if current_node.parent:
            current_node.val = self.level_sum_table[current_node.level] - current_node.parent.children_sum
        else:
            current_node.val = 0

        # Recursively update the right and left children
        self.depth_first_search_update(current_node.right)
        self.depth_first_search_update(current_node.left)

    def replace_value_in_tree(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        # Initialize root properties
        root.parent = None
        root.level = 0

        # Queue for BFS, starting with the root
        node_queue = [root]

        # Precompute the sum for each level using breadth-first search
        while node_queue:
            current_node = node_queue.pop(0)  # Dequeue the front node

            # Initialize or reset the sum of children's values for this node
            current_node.children_sum = 0
            # Add this node's value to the total for its level
            self.level_sum_table[current_node.level] += current_node.val

            # Process left child if exists
            if current_node.left:
                current_node.left.parent = current_node
                current_node.left.level = current_node.level + 1
                current_node.children_sum += current_node.left.val
                node_queue.append(current_node.left)

            # Process right child if exists
            if current_node.right:
                current_node.right.parent = current_node
                current_node.right.level = current_node.level + 1
                current_node.children_sum += current_node.right.val
                node_queue.append(current_node.right)

        # Use DFS to update node values based on computed level sums
        self.depth_first_search_update(root)
        return root

    replaceValueInTree = replace_value_in_tree
