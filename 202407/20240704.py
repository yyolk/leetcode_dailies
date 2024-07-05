# https://leetcode.com/problems/merge-nodes-in-between-zeros/


class Solution:
    """2181. Merge Nodes in Between Zeros

    You are given the `head` of a linked list, which contains a series of integers
    **separated** by `0`'s. The **beginning** and **end** of the linked list will have
    `Node.val == 0`.

    For **every** two consecutive `0`'s, **merge** all the nodes lying in between them
    into a single node whose value is the **sum** of all the merged nodes. The modified
    list should not contain any `0`'s.

    Return *the* `head` *of the modified linked list*.

    Definition for singly-linked list:

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def merge_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Skip the initial zero node
        current = head.next
        # This will be the new head of the resulting list
        dummy = ListNode(0)
        new_list_tail = dummy
        # Sum of values between zeros
        current_sum = 0

        while current:
            if current.val != 0:
                # Add value to the current sum
                current_sum += current.val
            else:
                if current_sum > 0:
                    # Create a new node with the current sum
                    new_node = ListNode(current_sum)
                    # Attach it to the new list
                    new_list_tail.next = new_node
                    # Move the tail to the new node
                    new_list_tail = new_node
                    # Reset the sum
                    current_sum = 0
            # Move to the next node in the original list
            current = current.next

        # Return the next of dummy since the first node is dummy
        return dummy.next

    mergeNodes = merge_nodes
