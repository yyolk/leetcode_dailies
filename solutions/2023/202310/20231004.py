# https://leetcode.com/problems/design-hashmap/
"""706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

* `MyHashMap()` initializes the object with an empty map.

* `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap.
If the `key` already exists in the map, update the corresponding `value`.

* `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1`
if this map contains no mapping for the `key`.

* `void remove(key)` removes the `key` and its corresponding `value` if the map
contains the mapping for the `key`.
"""


class MyHashMap:
    """A HashMap implemented without using any builtins for HashMaps.

    Proposed solution, using a pre-allocated list with all indexes within the
    constraints.

    This solution purposefully avoids using dict(...), per prompt instructions.
    """

    def __init__(self):
        # The maximum size based on the provided constraints
        self.size = 10_000_001
        # Allocate our buckets
        self.buckets = [-1] * self.size

    def put(self, key: int, value: int) -> None:
        """Insert a key, update the key if it exists.

        All values are updates, all keys are pre-allocated in accordance with
        constraints.

        Args:
            key (int): The index to map value to.
            value (int): The value to assign to index.
        """
        self.buckets[key] = value

    def get(self, key: int) -> int:
        """Returns the value to the mapped key, otherwise -1 is returned.

        All values were pre-allocated to -1, so -1 is the default case.

        Args:
            key (int): The index.

        Returns:
            int: -1 if the key doesn't exist, otherwise the value mapped to key.
        """
        return self.buckets[key]

    def remove(self, key: int) -> None:
        """Removes the key and it's corresponding value if the map contains it.

        Accomplished by re-assigning it to the default value, -1.

        Args:
            key (int): The index.
        """
        self.buckets[key] = -1
