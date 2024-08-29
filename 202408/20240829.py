# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class Solution:
    """947. Most Stones Removed with Same Row or Column

    On a 2D plane, we place `n` stones at some integer coordinate points. Each
    coordinate point may have at most one stone.

    A stone can be removed if it shares either **the same row or the same column** as
    another stone that has not been removed.

    Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the
    location of the `ith` stone, return *the largest possible number of stones that can
    be removed*.

    """

    def remove_stones(self, stones: list[list[int]]) -> int:
        # Initialize parent dict for Union-Find
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                # Path compression
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Union stones by row and column
        for x, y in stones:
            # Using ~y to avoid collision with x
            union(x, ~y)

        # Count unique roots, which represent islands of stones
        unique_roots = set()
        for x, y in stones:
            unique_roots.add(find(x))

        # The number of stones that can be removed is total stones minus unique roots
        return len(stones) - len(unique_roots)

    removeStones = remove_stones
