# https://leetcode.com/problems/linked-list-cycle/


class Solution:
    """141. Linked List Cycle

    Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached
    again by continuously following the\xa0`next`\xa0pointer. Internally, `pos`\xa0is used to denote
    the index of the node that\xa0tail's\xa0`next`\xa0pointer is connected to.\xa0**Note that\xa0`pos`\xa0is
    not passed as a parameter**.

    Return\xa0`true` *if there is a cycle in the linked list*. Otherwise, return `false`.
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ...
