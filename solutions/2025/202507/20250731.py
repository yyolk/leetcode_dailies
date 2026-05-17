# https://leetcode.com/problems/bitwise-ors-of-subarrays/


class Solution:
    """898. Bitwise ORs of Subarrays

    Given an integer array `arr`, return *the number of distinct bitwise ORs of all the
    non-empty subarrays of* `arr`.

    The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The
    bitwise OR of a subarray of one integer is that integer.

    A **subarray** is a contiguous non-empty sequence of elements within an array."""

    def subarray_bitwise_o_rs(self, arr: list[int]) -> int:
        # Initialize a set to store all unique bitwise OR results
        ans = set()
        # Initialize a set to store bitwise OR results for current subarrays ending at current element
        cur = set()
        # Iterate through each element in the input array
        for a in arr:
            # Start new set with current element as a single-element subarray
            new_cur = {a}
            # Compute bitwise OR of current element with each previous subarray OR result
            for o in cur:
                # Add the new bitwise OR result to new_cur
                new_cur.add(o | a)
            # Update cur to new_cur for the next iteration
            cur = new_cur
            # Add all current subarray OR results to the final answer set
            ans.update(cur)
        # Return the count of unique bitwise OR results
        return len(ans)

    subarrayBitwiseORs = subarray_bitwise_o_rs
