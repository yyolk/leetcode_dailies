# https://leetcode.com/problems/unique-binary-search-trees-ii/


class Solution:
    """95. Unique Binary Search Trees II

    Given an integer `n`, return *all the structurally unique **BST'**s (binary search
    trees), which has exactly* `n` *nodes of unique values from* `1` *to* `n`. Return
    the answer in **any order**.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def generate_trees(self, n: int) -> list[Optional[TreeNode]]:
        # If n is 0, return an empty list
        if n == 0:
            return []
        # Call the helper function to generate trees from 1 to n
        return self.generate_trees_helper(1, n)

    def generate_trees_helper(self, start, end):
        # Base case: if start > end, return a list containing None
        if start > end:
            return [None]
        result = []
        # Iterate over values from start to end
        for i in range(start, end + 1):
            # Generate left subtrees recursively for values less than i
            left_subtrees = self.generate_trees_helper(start, i - 1)
            # Generate right subtrees recursively for values greater than i
            right_subtrees = self.generate_trees_helper(i + 1, end)
            # Combine left and right subtrees for each value i
            for left in left_subtrees:
                for right in right_subtrees:
                    # Create a new root node with value i
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    # Add the tree with root node to the result list
                    result.append(root)
        return result

    generateTrees = generate_trees