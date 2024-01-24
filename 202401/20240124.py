# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/


class Solution:
    """1457. Pseudo-Palindromic Paths in a Binary Tree

    Given a binary tree where node values are digits from 1 to 9. A path in the binary
    tree is said to be **pseudo-palindromic** if at least one permutation of the node
    values in the path is a palindrome.

    *Return the number of **pseudo-palindromic** paths going from the root node to leaf
    nodes.*

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def pseudo_palindromic_paths(self, root: Optional[TreeNode]) -> int:
        def is_pseudo_palindrome(path_count):
            """Helper function to check if a list of counts represents a pseudo-palindrome."""
            odd_count = 0
            for count in path_count:
                if count % 2 == 1:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, path_count):
            """DFS function to traverse the binary tree and count pseudo-palindromic paths."""
            if not node:
                return 0

            # Increment count for the current node's value
            path_count[node.val - 1] += 1

            # Check if it's a leaf node, and if so, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                if is_pseudo_palindrome(path_count):
                    return 1
                else:
                    return 0

            # Recursively explore left and right subtrees
            total_paths = dfs(node.left, path_count.copy()) + dfs(node.right, path_count.copy())

            return total_paths

        # Call the DFS function starting from the root with an initial count array
        return dfs(root, [0] * 9)

    pseudoPalindromicPaths = pseudo_palindromic_paths
