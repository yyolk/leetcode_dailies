# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/


class Solution:
    """1171. Remove Zero Sum Consecutive Nodes from Linked List

    Given the `head` of a linked list, we repeatedly delete consecutive sequences of
    nodes that sum to `0` until there are no such sequences.

    After doing so, return the head of the final linked list.  You may return any such
    answer.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def remove_zero_sum_sublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle cases where the entire list is removed
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        # Dictionary to store the running sum and its corresponding node
        sum_dict = {0: dummy}

        while head:
            prefix_sum += head.val

            if prefix_sum in sum_dict:
                # Remove nodes with zero sum in between
                temp = sum_dict[prefix_sum].next
                temp_sum = prefix_sum + temp.val
                while temp != head:
                    del sum_dict[temp_sum]
                    temp = temp.next
                    temp_sum += temp.val
                sum_dict[prefix_sum].next = head.next
            else:
                sum_dict[prefix_sum] = head

            head = head.next

        return dummy.next

    removeZeroSumSublists = remove_zero_sum_sublists
