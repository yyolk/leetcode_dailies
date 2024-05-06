# https://leetcode.com/problems/remove-nodes-from-linked-list/
from typing import Optional


class Solution:
    """2487. Remove Nodes From Linked List

    You are given the `head` of a linked list.

    Remove every node which has a node with a greater value anywhere to the right side
    of it.

    Return *the* `head` *of the modified linked list.*

    Definition for singly-linked list::
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Reverse the linked list
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Traverse the reversed list and remove nodeswithsmaller values
        max_val = float("-inf")
        # Dummy node to handle the case of deleting hte head
        dummy = ListNode(0)
        dummy.next = prev
        current = dummy

        while current.next:
            if current.next.val < max_val:
                # Remove the node
                current.next = current.next.next
            else:
                max_val = current.next.val
                current = current.next

        # Reverse the modified list to get the final result
        prev, current = None, dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Prev now points to the head of the modified list.
        return prev

    removeNodes = remove_nodes
