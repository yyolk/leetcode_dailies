# https://leetcode.com/problems/smallest-string-starting-from-leaf/
from collections import deque
from typing import Optional


class Solution:
    """988. Smallest String Starting From Leaf

    You are given the `root` of a binary tree where each node has a value in the range
    `[0, 25]` representing the letters `'a'` to `'z'`.

    Return *the **lexicographically smallest** string that starts at a leaf of this tree
    and ends at the root*.

    As a reminder, any shorter prefix of a string is **lexicographically smaller**.

    * For example, `"ab"` is lexicographically smaller than `"aba"`.

    A leaf of a node is a node that has no children.

    Definition for a binary tree node::

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def num_to_char(self, number):
        # Converts a number to its corresponding character (in the range 'a' to 'z')
        return chr(ord("a") + number)

    def smallest_from_leaf(self, root: Optional[TreeNode]) -> str:
        # Initialize a queue and add the root node with its path (just the root's value)
        queue = deque()
        queue.append((root, self.num_to_char(root.val)))
        results = []

        # Traverse the tree using BFS
        while queue:
            # Get the current node and its path from the queue
            cur, path = queue.popleft()

            # If the current node is a leaf, add its path to the results list
            if not cur.left and not cur.right:
                # Reverse the path to get the correct order
                results.append(path[::-1])

            # If the current node has a left child, add it to the queue
            if cur.left:
                queue.append((cur.left, path + self.num_to_char(cur.left.val)))

            # If the current node has a right child, add it to the queue
            if cur.right:
                queue.append((cur.right, path + self.num_to_char(cur.right.val)))

        # Sort the results and return the first (smallest) string
        results.sort()
        return results[0]

    smallestFromLeaf = smallest_from_leaf
