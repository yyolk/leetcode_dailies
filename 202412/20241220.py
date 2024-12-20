# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """2415. Reverse Odd Levels of Binary Tree

    Given the `root` of a **perfect** binary tree, reverse the node values at each
    **odd** level of the tree.

    * For example, suppose the node values at level 3 are `[2,1,3,4,7,11,29,18]`, then
    it should become `[18,29,11,7,4,3,1,2]`.

    Return *the root of the reversed tree*.

    A binary tree is **perfect** if all parent nodes have two children and all leaves
    are on the same level.

    The **level** of a node is the number of edges along the path between it and the
    root node."""

    def reverse_odd_levels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Use a queue for level-order traversal
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            # Store nodes at current level
            nodes_at_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                nodes_at_level.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse values at odd levels
            if level % 2 == 1:
                left, right = 0, len(nodes_at_level) - 1
                while left < right:
                    nodes_at_level[left].val, nodes_at_level[right].val = nodes_at_level[right].val, nodes_at_level[left].val
                    left += 1
                    right -= 1
            
            level += 1
        
        return root

    reverseOddLevels = reverse_odd_levels
