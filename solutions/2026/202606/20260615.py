# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class Solution:
    """2095. Delete the Middle Node of a Linked List

    You are given the head of a linked list. Delete the middle node, and
    return the head of the modified linked list. The middle node of a linked
    list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
    where ⌊x⌋ denotes the largest integer less than or equal to x. For n=1,2,3,
    4, and 5 the middle nodes are 0,1,1,2, and 2 respectively.
    """
    def delete_middle(self, head: ListNode | None) -> ListNode | None:
        # n<=1: delete the only node (middle is index 0)
        if not head or not head.next:
            return None
        # slow points before middle; fast starts 2 nodes ahead
        slow = head
        fast = head.next.next
        # fast leads 2x until it cannot advance fully (positions middle)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # unlink middle: skip slow.next entirely
        slow.next = slow.next.next
        return head

    deleteMiddle = delete_middle