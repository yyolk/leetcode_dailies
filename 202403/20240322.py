# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


class Solution:
    """234. Palindrome Linked List

    Given the `head` of a singly linked list, return `true` *if it is a* *palindrome*
    *or* `false` *otherwise*.

    Definition for singly-linked list::
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverse_linked_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        if not head or not head.next:
            return True

        # Find the middle of the linked list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half_reversed = reverse_linked_list(slow)

        # Compare the first half with the reversed second half
        while second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next

        return True

    isPalindrome = is_palindrome
        