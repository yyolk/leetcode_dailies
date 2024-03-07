# https://leetcode.com/problems/middle-of-the-linked-list/


class Solution:
    """876. Middle of the Linked List

    Given the `head` of a singly linked list, return _the middle node of the linked list_.

    If there are two middle nodes, return *the second middle* node.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next    
    """
    def middle_node(self, head: ListNode | None) -> ListNode | None:
        # Check if the linked list is empty
        if not head:
            return None

        # Initialize slow and fast pointers
        slow = fast = head

        # Move the fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The slow pointer is now at the middle (or second middle) node
        return slow

    middleNode = middle_node