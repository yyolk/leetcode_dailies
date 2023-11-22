# https://leetcode.com/problems/find-mode-in-binary-search-tree/


class Solution:
    """501. Find Mode in Binary Search Tree

    Given the `root` of a binary search tree (BST) with duplicates, return *all the
    [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most
    frequently occurred element) in it*.

    If the tree has more than one mode, return them in **any order**.

    Assume a BST is defined as follows:

    * The left subtree of a node contains only nodes with keys **less than or equal to**
    the node's key.

    * The right subtree of a node contains only nodes with keys **greater than or equal
    to** the node's key.

    * Both the left and right subtrees must also be binary search trees.

    Definition for a binary tree node:

            class TreeNode:
                def __init__(self, val=0, left=None, right=None):
                    self.val = val
                    self.left = left
                    self.right = right
    """

    def find_mode(self, root: TreeNode | None) -> list[int]:
        """
        Find the mode(s) in a binary search tree (BST) with duplicates.

        Args:
            root: The root node of the BST.

        Returns:
            A list of mode(s) in the BST.
        """

        def inorder_traversal(node: TreeNode | None):
            """
            Perform an in-order traversal of the BST and populate the 'elements' list
            with node values.

            Args:
                node: The current node in the traversal.
            """
            if node:
                # Traverse the left subtree
                inorder_traversal(node.left)
                # Append the current node's value to the elements list
                elements.append(node.val)
                # Traverse the right subtree
                inorder_traversal(node.right)

        def find_modes(elements: list[int]) -> list[int]:
            """
            Find the mode(s) from the list of elements.

            Args:
                elements: list of elements from the BST.

            Returns:
                A list of mode(s).
            """
            modes = []
            max_freq = 0
            curr_val = None
            curr_freq = 0

            for val in elements:
                if val == curr_val:
                    curr_freq += 1
                else:
                    curr_val = val
                    curr_freq = 1

                if curr_freq > max_freq:
                    # Found a new mode, update modes
                    modes = [val]
                    max_freq = curr_freq
                elif curr_freq == max_freq:
                    # Current value has the same frequency as the modes, add it to the modes
                    modes.append(val)

            return modes

        # Initialize elements as an empty list
        elements: list[int] = []
        # Perform in-order traversal to populate elements
        inorder_traversal(root)
        # Find and return the modes
        return find_modes(elements)

    findMode = find_mode
