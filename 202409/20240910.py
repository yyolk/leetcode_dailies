# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/


class Solution:
    """2807. Insert Greatest Common Divisors in Linked List

    Given the head of a linked list `head`, in which each node contains an integer
    value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the
    **greatest common divisor** of them.

    Return *the linked list after insertion*.

    The **greatest common divisor** of two numbers is the largest positive integer that
    evenly divides both numbers.

    """

    def insert_greatest_common_divisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]: ...

    insertGreatestCommonDivisors = insert_greatest_common_divisors
