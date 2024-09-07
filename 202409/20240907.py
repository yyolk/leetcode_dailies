# https://leetcode.com/problems/linked-list-in-binary-tree/


class Solution:
    """1367. Linked List in Binary Tree

    Given a binary tree `root` and a linked list with `head` as the first node.

    Return True if all the elements in the linked list starting from the `head`
    correspond to some *downward path* connected in the binary tree otherwise return
    False.

    In this context downward path means a path that starts at some node and goes
    downwards.

    """

    def is_sub_path(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool: ...

    isSubPath = is_sub_path
