# https://leetcode.com/problems/linked-list-in-binary-tree/


class Solution:
    """1367. Linked List in Binary Tree

    Given a binary tree `root` and a linked list with `head` as the first node.

    Return True if all the elements in the linked list starting from the `head`
    correspond to some *downward path* connected in the binary tree otherwise return
    False.

    In this context downward path means a path that starts at some node and goes
    downwards.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    Definition for a binary tree node::

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def is_sub_path(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            # An empty list is a subpath of any tree
            return True
        if not root:
            # If tree is empty but list isn't, no path exists
            return False

        # Check if we can start the path from the current root or if we need to check its children
        return (
            self._check_path(head, root)
            or self.is_sub_path(head, root.left)
            or self.is_sub_path(head, root.right)
        )

    def _check_path(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # Base cases
        if not head:
            # All nodes in list matched
            return True
        if not node:
            # Tree ended before list
            return False

        # If current node matches head, check next in both structures
        if node.val == head.val:
            return self._check_path(head.next, node.left) or self._check_path(
                head.next, node.right
            )

        # Current node does not match, no need to proceed downward from here
        return False

    isSubPath = is_sub_path
