# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/


class Solution:
    """2816. Double a Number Represented as a Linked List

    You are given the `head` of a **non-empty** linked list representing a non-negative
    integer without leading zeroes.

    Return *the* `head` *of the linked list after **doubling** it*.

    Definition for singly-linked list::
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def double_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_carry(node: Optional[ListNode]) -> Optional[ListNode]:
            """A helper function to calculate carry and update node values."""
            # Base case: node is None, return 0
            if node is None:
                return 0
            
            # Recursively get carry from the next node
            val = node.val * 2 + get_carry(node.next)
            node.val = val % 10  # Update current node value
            return val // 10  # Return carry

        # Check if there is a carry from the most significant digit
        if get_carry(head) == 1:
            # If there is a carry, create a new node for the carry
            return ListNode(1, head)
        
        # Return the modified head of the list
        return head

    doubleIt = double_it
