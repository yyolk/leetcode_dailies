# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """2471. Minimum Number of Operations to Sort a Binary Tree by Level

    You are given the `root` of a binary tree with **unique values**.

    In one operation, you can choose any two nodes **at the same level** and swap their
    values.

    Return *the minimum number of operations needed to make the values at each level
    sorted in a **strictly increasing order***.

    The **level** of a node is the number of edges along the path between it and the
    root node*.*"""

    def minimum_operations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr: List[int]) -> int:
            # Get the sorted version of the array and track the indices
            sorted_arr = sorted((val, idx) for idx, val in enumerate(arr))
            visited = [False] * len(arr)
            swaps = 0

            for i in range(len(arr)):
                # If already visited or already in correct position, skip
                if visited[i] or sorted_arr[i][1] == i:
                    continue

                # Count the size of the cycle
                cycle_size = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = sorted_arr[j][1]
                    cycle_size += 1

                # Add (cycle_size - 1) to swaps
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        # Level-order traversal to collect values level by level
        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the minimum swaps for the current level
            total_swaps += min_swaps_to_sort(level_values)

        return total_swaps

    minimumOperations = minimum_operations
