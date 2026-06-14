# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


class Solution:
    """2130. Maximum Twin Sum of a Linked List

    In a linked list of size n, where n is even, the ith node (0-indexed) of the
    linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) -
    1. For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
    twin of node 2. These are the only nodes with twins for n = 4. The twin sum is
    defined as the sum of a node and its twin. Given the head of a linked list with
    even length, return the maximum twin sum of the linked list.

    Constraints:
    * The number of nodes in the list is an even integer in the range [2, 105].
    * 1 <= Node.val <= 105
    Definition for singly-linked list.
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next"""

    def pair_sum(self, head: ListNode | None) -> int:
        # slow/fast find middle: slow stops at start of second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half in-place
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # two pointers on first half + rev second half for max twin sum
        max_sum = 0
        first = head
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        return max_sum

    pairSum = pair_sum
