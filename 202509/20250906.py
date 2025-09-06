# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/


class Solution:
    """3495. Minimum Operations to Make Array Elements Zero

    You are given a 2D array `queries`, where `queries[i]` is of the form `[l, r]`. Each
    `queries[i]` defines an array of integers `nums` consisting of elements ranging from
    `l` to `r`, both **inclusive**.

    In one operation, you can:

    * Select two integers `a` and `b` from the array.

    * Replace them with `floor(a / 4)` and `floor(b / 4)`.

    Your task is to determine the **minimum** number of operations required to reduce
    all elements of the array to zero for each query. Return the sum of the results for
    all queries."""

    def min_operations(self, queries: list[list[int]]) -> int:
        def prefix(n: int) -> int:
            # Compute the sum of division counts from 1 to n
            if n <= 0:
                return 0
            res = 0
            # Start with 4^0 = 1
            pow4 = 1
            # Level starts at 1 for numbers 1 to 3
            level = 1
            while True:
                # Calculate next power of 4
                next_pow4 = pow4 * 4
                # Check if the full range up to next_pow4 - 1 is within n
                if next_pow4 - 1 <= n:
                    # Add contribution of full level: level * number of elements in this level
                    res += level * (next_pow4 - pow4)
                    # Update to next power
                    pow4 = next_pow4
                    # Increment level
                    level += 1
                else:
                    # Add partial contribution for the remaining numbers
                    res += level * (n - pow4 + 1)
                    break
            return res

        # Initialize total sum of operations
        total = 0
        for l, r in queries:
            # Calculate total division counts for range [l, r]
            sum_div = prefix(r) - prefix(l - 1)
            # Compute min operations as ceil(sum_div / 2)
            ops = (sum_div + 1) // 2
            # Accumulate the operations
            total += ops
        return total

    minOperations = min_operations
