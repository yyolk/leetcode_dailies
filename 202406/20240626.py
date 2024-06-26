# https://leetcode.com/problems/balance-a-binary-search-tree/


class Solution:
    """1382. Balance a Binary Search Tree

    Given the `root` of a binary search tree, return *a **balanced** binary search tree
    with the same node values*. If there is more than one answer, return **any of
    them**.

    A binary search tree is **balanced** if the depth of the two subtrees of every node
    never differs by more than `1`.

    Definition for a binary tree node:

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    """

    def balance_bst(self, root: TreeNode) -> TreeNode:
        # Step 1: Convert BST to sorted list using inorder traversal
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_list = inorder_traversal(root)
        
        # Step 2: Convert sorted list to balanced BST
        def sorted_list_to_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_list[mid])
            node.left = sorted_list_to_bst(left, mid - 1)
            node.right = sorted_list_to_bst(mid + 1, right)
            return node
        
        return sorted_list_to_bst(0, len(sorted_list) - 1)

    balanceBST = balance_bst
