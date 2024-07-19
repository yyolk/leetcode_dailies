# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/


class Solution:
    """1530. Number of Good Leaf Nodes Pairs

    You are given the `root` of a binary tree and an integer `distance`. A pair of two
    different **leaf** nodes of a binary tree is said to be good if the length of **the
    shortest path** between them is less than or equal to `distance`.

    Return *the number of good leaf node pairs* in the tree.

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def count_pairs(self, root: TreeNode, distance: int) -> int:
        # Helper function to perform DFS and return a dictionary of distances
        def dfs(node):
            if not node:
                return {}
            if not node.left and not node.right:
                return {0: 1}

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Count pairs where the sum of distances is <= distance
            count = 0
            for ld, lc in left_distances.items():
                for rd, rc in right_distances.items():
                    if ld + rd + 2 <= distance:
                        count += lc * rc

            # Update distances for the current node
            distances = {}
            for d, c in left_distances.items():
                if d + 1 <= distance:
                    distances[d + 1] = distances.get(d + 1, 0) + c
            for d, c in right_distances.items():
                if d + 1 <= distance:
                    distances[d + 1] = distances.get(d + 1, 0) + c

            self.pair_count += count
            return distances

        self.pair_count = 0
        dfs(root)
        return self.pair_count

    countPairs = count_pairs
