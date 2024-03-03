# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional


class Solution:
    """19. Remove Nth Node From End of List

    Given the `head` of a linked list, remove the `nth` node from the end of the list
    and return its head.

    """

    def remove_nth_from_end(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next

    removeNthFromEnd = remove_nth_from_end
