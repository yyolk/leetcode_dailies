# https://leetcode.com/problems/copy-list-with-random-pointer/
# import copy  # Possible to solve just using copy.deepcopy


class Solution:
    """138. Copy List with Random Pointer

    A linked list of length `n` is given such that each node contains an additional random
    pointer, which could point to any node in the list, or `null`.

    Construct a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of
    the list. The deep copy should consist of exactly `n` **brand new** nodes, where each
    new node has its value set to the value of its corresponding original node. Both the
    `next` and `random` pointer of the new nodes should point to new nodes in the copied
    list such that the pointers in the original list and copied list represent the same list
    state. **None of the pointers in the new list should point to nodes in the original
    list**.

    For example, if there are two nodes `X` and `Y` in the original list, where `X.random
    --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random
    --> y`.

    Return *the head of the copied linked list*.

    The linked list is represented in the input/output as a list of `n` nodes. Each node is
    represented as a pair of `[val, random_index]` where:

    * `val`: an integer representing `Node.val`

    * `random_index`: the index of the node (range from `0` to `n-1`) that the `random`
    pointer points to, or `null` if it does not point to any node.

    Your code will **only** be given the `head` of the original linked list.

    Definition for a Node:

        class Node:
            def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
                self.val = int(x)
                self.next = next
                self.random = random

    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """Performs a deepcopy of the list

        Args:
            Optional Node: The input head of the linked list to copy

        Returns:
            Optional Node: The head of the copied linked list
        """
        # # Using copy.deepcopy 51-54ms, +8 to +16ms difference
        # return copy.deepcopy(head)

        # Not using standard-library to assist, 34-46ms
        if not head:
            return None

        # Create new nodes and insert them right after the original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Set random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Separate the original and copied lists
        current = head
        new_head = head.next
        new_current = new_head
        while current:
            current.next = current.next.next
            current = current.next
            if new_current.next:
                new_current.next = new_current.next.next
                new_current = new_current.next

        return new_head
