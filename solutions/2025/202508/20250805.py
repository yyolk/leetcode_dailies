# https://leetcode.com/problems/fruits-into-baskets-ii/


class Solution:
    """3477. Fruits Into Baskets II

    You are given two arrays of integers, `fruits` and `baskets`, each of length `n`,
    where `fruits[i]` represents the **quantity** of the `ith` type of fruit, and
    `baskets[j]` represents the **capacity** of the `jth` basket.

    From left to right, place the fruits according to these rules:

    * Each fruit type must be placed in the **leftmost available basket** with a
    capacity **greater than or equal** to the quantity of that fruit type.

    * Each basket can hold **only one** type of fruit.

    * If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

    Return the number of fruit types that remain unplaced after all possible allocations
    are made."""

    def num_of_unplaced_fruits(self, fruits: list[int], baskets: list[int]) -> int:
        # Determine the number of fruit types (and baskets, since lengths are equal)
        n = len(fruits)
        # Handle the edge case where there are no fruits
        if n == 0:
            return 0
        # Initialize the segment tree array with size 4*n for safety
        tree = [0] * (4 * n)

        # Define the build function to construct the segment tree
        def build(node: int, start: int, end: int) -> None:
            # Base case: if the range is a single element
            if start == end:
                # Set the tree node to the basket capacity at this index
                tree[node] = baskets[start]
                # Exit the function
                return
            # Calculate the midpoint of the range
            mid = (start + end) // 2
            # Recursively build the left subtree
            build(2 * node, start, mid)
            # Recursively build the right subtree
            build(2 * node + 1, mid + 1, end)
            # Set the current node to the max of its children
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        # Define the update function to modify a value in the segment tree
        def update(node: int, start: int, end: int, idx: int, val: int) -> None:
            # Base case: if the range is a single element
            if start == end:
                # Update the tree node with the new value
                tree[node] = val
                # Exit the function
                return
            # Calculate the midpoint of the range
            mid = (start + end) // 2
            # If the index is in the left half, update left subtree
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            # Otherwise, update the right subtree
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            # Update the current node to the max of its children
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        # Define the function to find the leftmost basket with capacity >= x
        def find_leftmost(node: int, start: int, end: int, x: int) -> int:
            # If the max in this range is less than x, no suitable basket
            if tree[node] < x:
                return -1
            # Base case: if the range is a single element
            if start == end:
                # Return the index as it's suitable
                return start
            # Calculate the midpoint of the range
            mid = (start + end) // 2
            # Try to find in the left subtree first
            left_res = find_leftmost(2 * node, start, mid, x)
            # If found in left, return it
            if left_res != -1:
                return left_res
            # Otherwise, search in the right subtree
            return find_leftmost(2 * node + 1, mid + 1, end, x)

        # Build the segment tree with root at node 1, covering 0 to n-1
        build(1, 0, n - 1)
        # Initialize counter for unplaced fruits
        unplaced = 0
        # Iterate over each fruit quantity
        for f in fruits:
            # Find the leftmost suitable basket index for this fruit
            idx = find_leftmost(1, 0, n - 1, f)
            # If no suitable basket found
            if idx == -1:
                # Increment unplaced count
                unplaced += 1
            # Otherwise, mark the basket as used by setting to -1
            else:
                update(1, 0, n - 1, idx, -1)
        # Return the number of unplaced fruits
        return unplaced

    numOfUnplacedFruits = num_of_unplaced_fruits
