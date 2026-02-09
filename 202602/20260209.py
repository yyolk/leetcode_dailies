# https://leetcode.com/problems/balance-a-binary-search-tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """1382. Balance a Binary Search Tree
    
    Given the root of a binary search tree, return a balanced binary search tree
    with the same node values. If there is more than one answer, return any of
    them.
    
    A binary search tree is balanced if the depth of the two subtrees of every
    node never differs by more than 1.
    """
    def balance_bst(self, root: TreeNode | None) -> TreeNode | None:
        nodes: list[TreeNode] = []
        
        # Inorder traversal to collect nodes in sorted order
        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            # Traverse left subtree
            inorder(node.left)
            # Visit current node
            nodes.append(node)
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        
        # Build balanced BST by selecting middle element as root
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            # Choose middle node to minimize height
            mid = (left + right) // 2
            node = nodes[mid]
            
            # Recursively build left subtree from left half
            node.left = build(left, mid - 1)
            # Recursively build right subtree from right half
            node.right = build(mid + 1, right)
            
            return node
        
        return build(0, len(nodes) - 1)
    
    balanceBST = balance_bst