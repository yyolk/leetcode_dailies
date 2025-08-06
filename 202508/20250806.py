# https://leetcode.com/problems/fruits-into-baskets-iii/


class Solution:
    """3479. Fruits Into Baskets III

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
        # Get the length of the arrays (n is the number of fruits and baskets)
        n = len(fruits)
        # Initialize the segment tree array with size 4*n (standard for segment trees)
        tree = [0] * (4 * n)

        # Define the build function to construct the segment tree
        def build(node: int, start: int, end: int) -> None:
            # Base case: if the segment is a single element
            if start == end:
                # Set the tree node to the basket capacity at this index
                tree[node] = baskets[start]
                # Return from the function
                return
            # Calculate the midpoint of the segment
            mid = (start + end) // 2
            # Recursively build the left child
            build(2 * node, start, mid)
            # Recursively build the right child
            build(2 * node + 1, mid + 1, end)
            # Set the current node to the max of its children (since we need max capacity)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        # Define the function to find the leftmost basket with capacity >= val
        def find_leftmost(node: int, start: int, end: int, val: int) -> int:
            # If the max in this segment is less than val, no suitable basket
            if tree[node] < val:
                # Return -1 to indicate not found
                return -1
            # Base case: if the segment is a single element
            if start == end:
                # Return the index as it's suitable
                return start
            # Calculate the midpoint
            mid = (start + end) // 2
            # Try to find in the left child first (for leftmost)
            left = find_leftmost(2 * node, start, mid, val)
            # If found in left, return it
            if left != -1:
                return left
            # Otherwise, search in the right child
            return find_leftmost(2 * node + 1, mid + 1, end, val)

        # Define the update function to set a basket's capacity to newval (default 0)
        def update(node: int, start: int, end: int, idx: int, newval: int = 0) -> None:
            # Base case: if the segment is the target index
            if start == end:
                # Update the tree node to newval
                tree[node] = newval
                # Return from the function
                return
            # Calculate the midpoint
            mid = (start + end) // 2
            # If the index is in the left half
            if idx <= mid:
                # Recur to left child
                update(2 * node, start, mid, idx, newval)
            # Otherwise, in the right half
            else:
                # Recur to right child
                update(2 * node + 1, mid + 1, end, idx, newval)
            # Update current node to max of children
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        # Build the segment tree for the entire range
        build(1, 0, n - 1)
        # Initialize counter for unplaced fruits
        unplaced = 0
        # Iterate over each fruit quantity
        for f in fruits:
            # Find the leftmost suitable basket index
            idx = find_leftmost(1, 0, n - 1, f)
            # If no suitable basket found
            if idx == -1:
                # Increment unplaced count
                unplaced += 1
            # Otherwise
            else:
                # Update the basket to 0 (used)
                update(1, 0, n - 1, idx)
        # Return the number of unplaced fruits
        return unplaced

    numOfUnplacedFruits = num_of_unplaced_fruits
