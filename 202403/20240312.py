# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/


class Solution:
    """1171. Remove Zero Sum Consecutive Nodes from Linked List

    Given the `head` of a linked list, we repeatedly delete consecutive sequences of
    nodes that sum to `0` until there are no such sequences.

    After doing so, return the head of the final linked list.  You may return any such
    answer.

    """

    def remove_zero_sum_sublists(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]: ...

    removeZeroSumSublists = remove_zero_sum_sublists
