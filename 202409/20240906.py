# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


class Solution:
    """3217. Delete Nodes From Linked List Present in Array

    You are given an array of integers `nums` and the `head` of a linked list. Return
    the `head` of the modified linked list after **removing** all nodes from the linked
    list that have a value that exists in `nums`.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def modified_list(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookup time
        num_set = set(nums)

        # Dummy node to handle the case where the head might be removed
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val in num_set:
                # Skip the node by moving current.next to the next of next
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        # Return the new head, which might be the dummy if all nodes were removed
        return dummy.next if dummy.next else None

    modifiedList = modified_list
