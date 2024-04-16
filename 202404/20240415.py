# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional


class Solution:
    """129. Sum Root to Leaf Numbers

    You are given the `root` of a binary tree containing digits from `0` to `9` only.

    Each root-to-leaf path in the tree represents a number.

    * For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

    Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that
    the answer will fit in a **32-bit** integer.

    A **leaf** node is a node with no children.

    Definition for a binary tree node::

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        
        def dfs(node, current_sum):
            nonlocal total_sum
            if not node:
                return
            
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:  # Leaf node
                total_sum += current_sum
                return
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        dfs(root, 0)
        return total_sum

    sumNumbers = sum_numbers
