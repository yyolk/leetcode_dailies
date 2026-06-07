# https://leetcode.com/problems/zero-array-transformation-iii/
import heapq


class Solution:
    """3362. Zero Array Transformation III

    You are given an integer array `nums` of length `n` and a 2D array `queries` where
    `queries[i] = [li, ri]`.

    Each `queries[i]` represents the following action on `nums`:

    * Decrement the value at each index in the range `[li, ri]` in `nums` by **at
    most**1.

    * The amount by which the value is decremented can be chosen **independently** for
    each index.

    A **Zero Array** is an array with all its elements equal to 0.

    Return the **maximum** number of elements that can be removed from `queries`, such
    that `nums` can still be converted to a **zero array** using the *remaining*
    queries. If it is not possible to convert `nums` to a **zero array**, return -1."""

    def max_removal(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        if n == 0:
            return len(queries)

        # Sort queries by start index
        queries.sort(key=lambda x: x[0])

        # Max-heap for queries, using -ri for largest ri first
        H = []
        # Min-heap for endpoints where coverage decreases
        end_points = []
        current_coverage = 0
        selected = 0
        k = 0  # Index for next query to consider

        for j in range(n):
            # Add queries that start at or before j
            while k < len(queries) and queries[k][0] <= j:
                li, ri = queries[k]
                heapq.heappush(H, (-ri, li))
                k += 1

            # Decrease coverage for queries ending before j
            while end_points and end_points[0] <= j:
                heapq.heappop(end_points)
                current_coverage -= 1

            # Ensure coverage meets nums[j]
            while current_coverage < nums[j]:
                if not H:
                    return -1
                # Discard queries that end before j
                while H and -H[0][0] < j:
                    heapq.heappop(H)
                if not H:
                    return -1
                ri, li = -H[0][0], H[0][1]
                heapq.heappop(H)
                selected += 1
                current_coverage += 1
                if ri + 1 < n:
                    heapq.heappush(end_points, ri + 1)

        return len(queries) - selected

    maxRemoval = max_removal
