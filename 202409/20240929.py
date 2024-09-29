# https://leetcode.com/problems/all-oone-data-structure/


class Node:
    """Linked list implementation."""
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    """432. All O`one Data Structure

    Design a data structure to store the strings' count with the ability to return the
    strings with minimum and maximum counts.

    Implement the `AllOne` class:

    * `AllOne()` Initializes the object of the data structure.

    * `inc(String key)` Increments the count of the string `key` by `1`. If `key` does
    not exist in the data structure, insert it with count `1`.

    * `dec(String key)` Decrements the count of the string `key` by `1`. If the count of
    `key` is `0` after the decrement, remove it from the data structure. It is
    guaranteed that `key` exists in the data structure before the decrement.

    * `getMaxKey()` Returns one of the keys with the maximal count. If no element
    exists, return an empty string `""`.

    * `getMinKey()` Returns one of the keys with the minimum count. If no element
    exists, return an empty string `""`.

    **Note** that each function must run in `O(1)` average time complexity.

    Your AllOne object will be instantiated and called as such:
        obj = AllOne()
        obj.inc(key)
        obj.dec(key)
        param_3 = obj.getMaxKey()
        param_4 = obj.getMinKey()
    """
    def __init__(self):
        # Sentinel nodes for head and tail of the doubly linked list
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        # Key to node mapping for O(1) access
        self.key_to_node = {}

    def _add_node_after(self, node, prev_node):
        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next.prev = node
        prev_node.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # If the key is new, and if there's no node for count 1, create one
            if self.head.next.count != 1:
                self._add_node_after(Node(1), self.head)
            self.key_to_node[key] = self.head.next
            self.key_to_node[key].keys.add(key)
        else:
            current_node = self.key_to_node[key]
            next_count = current_node.count + 1
            if current_node.next.count != next_count:
                new_node = Node(next_count)
                self._add_node_after(new_node, current_node)
            else:
                new_node = current_node.next
            
            new_node.keys.add(key)
            self.key_to_node[key] = new_node
            
            # Clean up the old count
            current_node.keys.remove(key)
            if not current_node.keys:
                self._remove_node(current_node)

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return  # Key does not exist

        current_node = self.key_to_node[key]
        if current_node.count == 1:
            del self.key_to_node[key]
            current_node.keys.remove(key)
        else:
            prev_count = current_node.count - 1
            if current_node.prev.count != prev_count:
                new_node = Node(prev_count)
                self._add_node_after(new_node, current_node.prev)
            else:
                new_node = current_node.prev
            
            new_node.keys.add(key)
            self.key_to_node[key] = new_node
            
            current_node.keys.remove(key)

        # Remove the node if it's empty
        if not current_node.keys:
            self._remove_node(current_node)

    def get_max_key(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    getMaxKey = get_max_key

    def get_min_key(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""

    getMinKey = get_min_key