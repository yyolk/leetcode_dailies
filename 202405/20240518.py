# https://leetcode.com/problems/distribute-coins-in-binary-tree/


class Solution:
    """979. Distribute Coins in Binary Tree

    You are given the `root` of a binary tree with `n` nodes where each `node` in the
    tree has `node.val` coins. There are `n` coins in total throughout the whole tree.

    In one move, we may choose two adjacent nodes and move one coin from one node to
    another. A move may be from parent to child, or from child to parent.

    Return *the **minimum** number of moves required to make every node have **exactly**
    one coin*.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def distribute_coins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Process left and right subtrees
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # Total moves is the absolute value of excess coins moved in both subtrees
            self.moves += abs(left_excess) + abs(right_excess)
            
            # Return the number of excess coins in this subtree
            # node.val - 1 is the excess/deficit of coins at the current node
            return node.val + left_excess + right_excess - 1
        
        dfs(root)
        return self.moves

    distributeCoins = distribute_coins
