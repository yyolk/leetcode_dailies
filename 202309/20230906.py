# https://leetcode.com/problems/split-linked-list-in-parts/


class Solution:
    """725. Split Linked List in Parts

    Given the `head` of a singly linked list and an integer `k`, split the linked list into
    `k` consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should have a size
    differing by more than one. This may lead to some parts being null.

    The parts should be in the order of occurrence in the input list, and parts occurring
    earlier should always have a size greater than or equal to parts occurring later.

    Return *an array of the* `k` *parts*.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        """Split input linked list into parts

        Proposed solution using nested iteration and divmod(...)

        Args:
            head (Optional ListNode): the input, the first ListNode of a singly linked list
            k (int): the requested number of parts to split the linked list into

        Returns:
            List of Optional ListNode: the resulting list containing the parts the
                input was split into
        """
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the size of each part and the number of larger parts
        part_size, extra_parts = divmod(length, k)

        result = []
        # Rewind our walk to calculate the length
        current = head
        for i in range(k):
            # Keep a reference to the head to append to our results
            part_head = current
            # This part size is 1 bigger unless we've hit the threshold of our divmod remainder
            part_size_temp = part_size + (1 if i < extra_parts else 0)

            # Walk the ListNode the length of our part_size_temp, until there isn't any
            for j in range(part_size_temp - 1):
                if current:
                    current = current.next

            # Split the ListNode here, if not None.
            # It will be the new part_head on next(...)
            if current:
                current.next, current = None, current.next

            # Append this ListNode's head to the result List
            result.append(part_head)

        return result
