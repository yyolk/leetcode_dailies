# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
import heapq

from typing import Optional
from collections import deque


class Solution:
    """2583. Kth Largest Sum in a Binary Tree

    You are given the `root` of a binary tree and a positive integer `k`.

    The **level sum** in the tree is the sum of the values of the nodes that are on the
    **same** level.

    Return *the* `kth` ***largest** level sum in the tree (not necessarily distinct)*.
    If there are fewer than `k` levels in the tree, return `-1`.

    **Note** that two nodes are on the same level if they have the same distance from
    the root.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def kth_largest_level_sum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        # Use BFS to calculate sum at each level
        level_sums = []
        queue = deque([(root, 0)])  # Each item is (node, level)
        
        while queue:
            node, level = queue.popleft()
            
            # If this is a new level, add a new sum to level_sums
            if level == len(level_sums):
                level_sums.append(0)
            
            # Add current node's value to its level sum
            level_sums[level] += node.val
            
            # Add children to the queue if they exist
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Check if there are at least k levels
        if k > len(level_sums):
            return -1
        
        # Use a min heap to keep track of the k largest sums
        return heapq.nlargest(k, level_sums)[-1] if k > 0 else -1

    kthLargestLevelSum = kth_largest_level_sum
