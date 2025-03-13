# https://leetcode.com/problems/zero-array-transformation-ii/


class Solution:
    """3356. Zero Array Transformation II

    You are given an integer array `nums` of length `n` and a 2D array `queries` where
    `queries[i] = [li, ri, vali]`.

    Each `queries[i]` represents the following action on `nums`:

    * Decrement the value at each index in the range `[li, ri]` in `nums` by **at most**
    `vali`.

    * The amount by which each value is decremented can be chosen **independently** for
    each index.

    A **Zero Array** is an array with all its elements equal to 0.

    Return the **minimum** possible **non-negative** value of `k`, such that after
    processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**.
    If no such `k` exists, return -1."""

    def min_zero_array(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)  # Length of the input array
        m = len(queries)  # Number of queries

        # Initialize difference array to track range updates
        delta = [0] * (n + 1)

        # Reverse queries to process in original order via popping
        q = queries[::-1]

        # Current cumulative decrement
        cur = 0

        # Process each element in nums
        for i, x in enumerate(nums):
            # Add the delta at this index to the cumulative decrement
            cur += delta[i]

            # Accept queries until cur is sufficient to make nums[i] zero
            while q and cur < x:
                l, r, height = q.pop()  # Get the next query
                if r >= i:  # Query affects this index or beyond
                    if l <= i:  # Query includes current index
                        cur += height  # Apply decrement now
                    else:  # Query starts after current index
                        delta[l] += height  # Defer decrement to later
                    if r + 1 < n:  # Ensure we don’t go out of bounds
                        delta[r + 1] -= height  # End the range effect

            # If we can’t make nums[i] zero, it’s impossible
            if cur < x:
                return -1

        # Return the number of queries used
        return m - len(q)

    minZeroArray = min_zero_array
