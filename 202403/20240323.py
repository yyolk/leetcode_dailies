# https://leetcode.com/problems/reorder-list/
from typing import Optional


class Solution:
    """143. Reorder List

    You are given the head of a singly linked-list. The list can be represented as:

    ```

    L0 → L1 → ... → Ln - 1 → Ln

    ```

    *Reorder the list to be on the following form:*

    ```

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → ...

    ```

    You may not modify the values in the list's nodes. Only nodes themselves may be
    changed.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def reorder_list(self, head: Optional[ListNode]):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list using the slow and fast pointer technique
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list starting from the middle
        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = None

        # Step 3: Merge the first half and the reversed second half of the list
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    reorderList = reorder_list