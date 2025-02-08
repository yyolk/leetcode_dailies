# https://leetcode.com/problems/design-a-number-container-system/
"""2434. Design a Number Container System

Design a number container system that can do the following:

* **Insert** or **Replace** a number at the given index in the system.

* **Return** the smallest index for the given number in the system.

Implement the `NumberContainers` class:

* `NumberContainers()` Initializes the number container system.

* `void change(int index, int number)` Fills the container at `index` with the
`number`. If there is already a number at that `index`, replace it.

* `int find(int number)` Returns the smallest index for the given `number`, or `-1`
if there is no index that is filled by `number` in the system.

Your NumberContainers object will be instantiated and called as such:

    obj = NumberContainers()
    obj.change(index,number)
    param_2 = obj.find(number)
"""

import heapq


class NumberContainers:

    def __init__(self):
        # Maps index to number
        self.index_to_number = {}
        # Maps number to a min-heap of indices
        self.number_to_indices = {}

    def change(self, index: int, number: int) -> None:
        # Set number for index
        self.index_to_number[index] = number

        # Update the number_to_indices mapping
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            # No index with number
            return -1

        positive_indices = self.number_to_indices[number]
        while positive_indices:
            # Check lowest index
            minimum_index = positive_indices[0]
            if self.index_to_number[minimum_index] == number:
                # Valid index found number at index
                return minimum_index

            # Invalid index, new number at index
            heapq.heappop(positive_indices)

        # No valid index found
        return -1
