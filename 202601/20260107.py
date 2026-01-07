# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalSum = 0
        self.max = 0

    def dfs(self, root):
        if root is None:
            return 0
        return root.val + self.dfs(root.left) + self.dfs(root.right)

    def postOrder(self, root):
        if root is None:
            return 0
        sum = root.val + self.postOrder(root.left) + self.postOrder(root.right)
        self.max = self.max if self.max > (self.totalSum - sum) * sum else (self.totalSum - sum) * sum
        return sum

    def maxProduct(self, root):
        self.totalSum = self.dfs(root)
        self.max = 0
        self.postOrder(root)
        return int(self.max % 1000000007)