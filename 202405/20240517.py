# https://leetcode.com/problems/delete-leaves-with-a-given-value/


class Solution:
    """1325. Delete Leaves With a Given Value

    Given a binary tree `root` and an integer `target`, delete all the **leaf nodes**
    with value `target`.

    Note that once you delete a leaf node with value `target`**,** if its parent node
    becomes a leaf node and has the value `target`, it should also be deleted (you need
    to continue doing that until you cannot).

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def remove_leaf_nodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        # If the root is None, return None (base case for recursion)
        if not root:
            return None

        # Recursively call the function on the left and right children
        root.left = self.remove_leaf_nodes(root.left, target)
        root.right = self.remove_leaf_nodes(root.right, target)

        # If the current node is a leaf and its value is the target, return None to remove it
        if not root.left and not root.right and root.val == target:
            return None

        # Return the current node
        return root

    removeLeafNodes = remove_leaf_nodes
