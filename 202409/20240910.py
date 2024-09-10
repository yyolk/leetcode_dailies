# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
from math import gcd


class Solution:
    """2807. Insert Greatest Common Divisors in Linked List

    Given the head of a linked list `head`, in which each node contains an integer
    value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the
    **greatest common divisor** of them.

    Return *the linked list after insertion*.

    The **greatest common divisor** of two numbers is the largest positive integer that
    evenly divides both numbers.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def insert_greatest_common_divisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # If the list is empty or has only one node, no insertion is needed
        if not head or not head.next:
            return head
        
        # Start with the head of the list
        current = head
        
        while current and current.next:
            # Find the next node
            next_node = current.next
            
            # Calculate GCD of current node and next node
            gcd_value = gcd(current.val, next_node.val)
            
            # Create a new node with the GCD value
            gcd_node = ListNode(gcd_value)
            
            # Insert the new GCD node between current and next_node
            current.next = gcd_node
            gcd_node.next = next_node
            
            # Move to the original next node to continue the process
            current = next_node
        
        return head

    insertGreatestCommonDivisors = insert_greatest_common_divisors
