# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """3217. Delete Nodes From Linked List Present in Array

    You are given an array of integers nums and the head of a linked list.
    Return the head of the modified linked list after removing all nodes from
    the linked list that have a value that exists in `nums`.
    """
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        # Create a set for O(1) lookups of values to remove
        num_set = set(nums)
        
        # Use a dummy node to handle head removal easily
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers: prev starts at dummy, current at head
        prev = dummy
        current = head
        
        # Traverse the list
        while current:
            # If current value is in the set, skip it by updating prev.next
            if current.val in num_set:
                prev.next = current.next
            else:
                # Otherwise, move prev to current
                prev = current
            # Always advance current
            current = current.next
        
        # Return the new head, which is dummy.next
        return dummy.next
