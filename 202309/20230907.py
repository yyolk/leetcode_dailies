# https://leetcode.com/problems/reverse-linked-list-ii/


class Solution:
    """92. Reverse Linked List II

    Given the `head` of a singly linked list and two integers `left` and `right` where `left
    <= right`, reverse the nodes of the list from position `left` to position `right`, and
    return *the reversed list*.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """Reverse slice of input ListNode

        Proposed solution.

        Takes in a ListNode and reverses the elements between `left` and `right` (inclusive)

        Args:
            head (Optional ListNode): the input ListNode to manipulate
            left (int): the start of the slice of elements to reverse
            right (int): the end of the slice of elements to reverse

        Returns:
            Optional ListNode: the manipulated ListNode result after reversing the elements
        """
        dummy = ListNode(0)
        dummy.next = head
        # Node before the left position
        prev = dummy
        # Current node
        current = head

        # Move to the node just before the left position
        for _ in range(left - 1):
            prev = current
            current = current.next

        # Reverse the sublist between left and right
        prev_tail = prev
        current_tail = current
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Connect the reversed sublist to the original
        prev_tail.next = prev
        current_tail.next = current

        return dummy.next
