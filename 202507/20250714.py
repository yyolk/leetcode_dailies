# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """1290. Convert Binary Number in a Linked List to Integer

    Given `head` which is a reference node to a singly-linked list. The value of each
    node in the linked list is either `0` or `1`. The linked list holds the binary
    representation of a number.

    Return the *decimal value* of the number in the linked list.

    The **most significant bit** is at the head of the linked list."""

    def get_decimal_value(self, head: ListNode | None) -> int:
        result = 0
        current = head
        while current:
            result = result * 2 + current.val
            current = current.next
        return result

    getDecimalValue = get_decimal_value
