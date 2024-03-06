# https://leetcode.com/problems/linked-list-cycle/


class Solution:
    """141. Linked List Cycle

    Given `head`, the head of a linked list, determine if the linked list has a cycle in
    it.

    There is a cycle in a linked list if there is some node in the list that can be
    reached again by continuously following the `next` pointer. Internally, `pos` is
    used to denote the index of the node that tail's `next` pointer is connected to.
    **Note that `pos` is not passed as a parameter**.

    Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

    """

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return False

        # Initialize two pointers, slow and fast
        slow = head
        fast = head.next

        # Traverse the linked list using Floyd's Tortoise and Hare algorithm
        while fast and fast.next:
            # If there is a cycle, the fast pointer will eventually catch up with the slow pointer
            if slow == fast:
                return True

            # Move slow pointer one step at a time
            slow = slow.next
            # Move fast pointer two steps at a time
            fast = fast.next.next

        # If no cycle is found, return False
        return False

    hasCycle = has_cycle
