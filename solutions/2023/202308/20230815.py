# https://leetcode.com/problems/partition-list/


class Solution:
    """86. Partition List

    Given the `head` of a linked list and a value `x`, partition it such that all nodes
    **less than** `x` come before nodes **greater than or equal** to `x`.

    You should **preserve** the original relative order of the nodes in each of the two
    partitions.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """Partition the input linked list to fit the rules.

        Partition the input linked list to fit the rules such to all nodes less than x
        come before all nodes greater than x

        Args:
            head: The input linked list.
            x: The input value to partition the linked list in accordance with the
                partition rules.

        Returns:
            The newly partitioned linked list.
        """
        # Create two dummy nodes for the two partitions.
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)

        # Pointers for the current nodes in the two partitions.
        before = before_dummy
        after = after_dummy

        # Traverse the original linked list.
        while head:
            # If the current node's value is less than x, add to the "before" partition.
            if head.val < x:
                before.next = head
                before = before.next
            # If the current node's value is greater than or equal to x, add to the
            # "after" partition.
            else:
                after.next = head
                after = after.next

            # Move to the next node in the original list.
            head = head.next

        # Connect the "before" and "after" partitions.
        before.next = after_dummy.next
        # Set the end of the "after" partition to None.
        after.next = None

        # The result is the combined list.
        return before_dummy.next

    partition = partition
