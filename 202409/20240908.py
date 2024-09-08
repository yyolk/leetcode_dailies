# https://leetcode.com/problems/split-linked-list-in-parts/


class Solution:
    """725. Split Linked List in Parts

    Given the `head` of a singly linked list and an integer `k`, split the linked list
    into `k` consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should have a
    size differing by more than one. This may lead to some parts being null.

    The parts should be in the order of occurrence in the input list, and parts
    occurring earlier should always have a size greater than or equal to parts occurring
    later.

    Return *an array of the* `k` *parts*.

    """

    def split_list_to_parts(
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]: ...

    splitListToParts = split_list_to_parts
