# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """865. Smallest Subtree with all the Deepest Nodes

    Given the root of a binary tree, the depth of each node is the shortest
    distance to the root.

    Return the smallest subtree such that it contains all the deepest nodes
    in the original tree.

    A node is called the deepest if it has the largest depth possible among
    any node in the entire tree.

    The subtree of a node is a tree consisting of that node, plus the set of
    all descendants of that node.
    """
    def subtree_with_all_deepest(self, root: TreeNode | None) -> TreeNode | None:
        def helper(node: TreeNode | None) -> tuple[TreeNode | None, int]:
            # Base case: empty subtree has height -1
            if not node:
                return None, -1
            
            # Post-order: process left and right subtrees
            left_lca, left_h = helper(node.left)
            right_lca, right_h = helper(node.right)
            
            # Left subtree deeper -> all deepest nodes in left
            if left_h > right_h:
                return left_lca, left_h + 1
            
            # Right subtree deeper -> all deepest nodes in right
            if right_h > left_h:
                return right_lca, right_h + 1
            
            # Heights equal -> deepest nodes in both sides (or leaf)
            # Current node is the LCA of all deepest nodes in this subtree
            return node, left_h + 1
        
        # Return only the LCA node from the full tree
        lca, _ = helper(root)
        return lca
    
    subtreeWithAllDeepest = subtree_with_all_deepest