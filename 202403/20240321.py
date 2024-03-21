# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class Solution:
    """206. Reverse Linked List

    Given the `head` of a singly linked list, reverse the list, and return *the reversed
    list*.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next    

    """

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        # Previous node (initialized to None for the first node)
        prev = None
        # Current node (starts from the head of the original list)
        current = head

        while current:
            # Save the next node before changing the current node's pointer
            next_node = current.next

            # Reverse the pointer of the current node to point to the previous node
            current.next = prev

            # Move the prev pointer to the current node and the current pointer to the next node
            prev = current
            current = next_node

        # Return the new head of the reversed list (which is the last node of the original list)
        return prev

    reverseList = reverse_list
