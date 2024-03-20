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

    """

    def merge_in_between(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode: ...

    mergeInBetween = merge_in_between
