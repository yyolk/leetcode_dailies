# https://leetcode.com/problems/rotate-list/

class Solution:
    """61. Rotate List
    
    Given the head of a linked list, rotate the list to the right by k places.
    """
    def rotate_right(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        # Find length n and tail of the list
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        # Reduce k to effective rotations
        k %= n
        if k == 0:
            return head

        # Connect tail to head making it circular
        tail.next = head

        # Advance to the new tail (n - k - 1 steps from head)
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # Set new head and break the link at new tail
        new_head = new_tail.next
        new_tail.next = None

        return new_head

    rotateRight = rotate_right