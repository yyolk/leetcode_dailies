# https://leetcode.com/problems/linked-list-cycle/


class Solution:
    """141. Linked List Cycle

    Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached
    again by continuously following the `next` pointer. Internally, `pos` is used to denote
    the index of the node that tail's `next` pointer is connected to. **Note that `pos` is
    not passed as a parameter**.

    Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

    
    Definition for singly-linked list.
    
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None
    
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Determines if the input linked-list has a cycle in it

        Proposed solution uses Floyd's tortoise and hare algorithm
        https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare

        Args:
            head (Optional ListNode): the input linked-list

        Returns:
            bool: whether the input linked list has a cycle in it
        
        """
        # Check if the input linked list is empty or has only one node (no cycle possible)
        if not head or not head.next:
            return False

        # Initialize two pointers: tortoise and hare
        # Tortoise starts at the head
        tortoise = head
        # Hare starts one step ahead of the tortoise
        hare = head.next

        # Every step, determine if the tortoise and hare meet
        while tortoise != hare:
            # If the hare reaches the end of the list there is no cycle
            if not hare or not hare.next:
                return False

            # Move the tortoise one step ahead
            tortoise = tortoise.next
            # Move the hare two steps ahead
            hare = hare.next.next

        # If the tortoise and hare meet, there is a cycle
        return True
