# https://leetcode.com/problems/merge-in-between-linked-lists/


class Solution:
    """1669. Merge In Between Linked Lists

    You are given two linked lists: `list1` and `list2` of sizes `n` and `m`
    respectively.

    Remove `list1`'s nodes from the `ath` node to the `bth` node, and put `list2` in
    their place.

    The blue edges and nodes in the following figure indicate the result:

    ![](https://assets.leetcode.com/uploads/2020/11/05/fig1.png)

    *Build the result list and return its head.*

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def merge_in_between(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        # Initialize pointers
        ptr = list1  # Pointer to ath node
        for _ in range(a - 1):
            ptr = ptr.next  # Move ptr to the node before ath

        qtr = ptr.next  # Pointer to node after bth
        for _ in range(b - a + 1):
            qtr = qtr.next  # Move qtr to the node after bth

        # Connect list1 from ath to list2
        ptr.next = list2

        # Traverse list2 to find its tail node
        while list2.next:
            list2 = list2.next

        # Connect the tail node of list2 to qtr in list1
        list2.next = qtr

        return list1

    mergeInBetween = merge_in_between
