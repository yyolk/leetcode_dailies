# https://leetcode.com/problems/find-bottom-left-tree-value/


class Solution:
    """513. Find Bottom Left Tree Value

    Given the `root` of a binary tree, return the leftmost value in the last row of the
    tree.

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        # Use a queue for level-order traversal
        queue = deque([root])
        
        # Iterate level by level
        while queue:
            level_size = len(queue)
            
            # Initialize leftmost value at each level
            leftmost_value = queue[0].val
            
            for _ in range(level_size):
                current_node = queue.popleft()
                
                # Update leftmost value if it's the first node in the current level
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        
        return leftmost_value

    findBottomLeftValue = find_bottom_left_value
