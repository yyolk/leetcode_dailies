# https://leetcode.com/problems/product-of-the-last-k-numbers/
"""1477. Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of
the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

* `ProductOfNumbers()` Initializes the object with an empty stream.

* `void add(int num)` Appends the integer `num` to the stream.

* `int getProduct(int k)` Returns the product of the last `k` numbers in the current
list. You can assume that always the current list has at least `k` numbers.

The test cases are generated so that, at any time, the product of any contiguous
sequence of numbers will fit into a single 32-bit integer without overflowing.

Your FindElements object will be instantiated and called as such:

    obj = FindElements(root)
    param_1 = obj.find(target)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode | None):
        # Set to store recovered node values for O(1) lookup
        self.values = set()

        # DFS helper to assign values and collect them
        def recover(node, val):
            # If node exists, process it
            if node:
                # Assign computed value to node
                node.val = val
                # Add value to set for quick lookup
                self.values.add(val)
                # Recover left child with 2x + 1
                recover(node.left, 2 * val + 1)
                # Recover right child with 2x + 2
                recover(node.right, 2 * val + 2)

        # If root exists, start recovery from value 0
        if root:
            recover(root, 0)

    def find(self, target: int) -> bool:
        # Check if target exists in set, O(1) average time
        return target in self.values
