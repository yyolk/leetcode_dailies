# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
from collections import Counter


class Solution:
    """2598. Smallest Missing Non-negative Integer After Operations

    You are given a **0-indexed** integer array `nums` and an integer `value`.

    In one operation, you can add or subtract `value` from any element of `nums`.

    * For example, if `nums = [1,2,3]` and `value = 2`, you can choose to subtract
    `value` from `nums[0]` to make `nums = [-1,2,3]`.

    The MEX (minimum excluded) of an array is the smallest missing **non-negative**
    integer in it.

    * For example, the MEX of `[-1,2,3]` is `0` while the MEX of `[1,0,3]` is `2`.

    Return *the maximum MEX of* `nums` *after applying the mentioned operation **any
    number of times***."""

    def find_smallest_integer(self, nums: list[int], value: int) -> int:
        # Compute frequency of each residue modulo value
        freq = Counter(num % value for num in nums)
        # Start from potential MEX 0
        mex = 0
        while True:
            # Compute required residue for current mex
            r = mex % value
            # If a worker is available for this residue, use it
            if freq[r] > 0:
                # Decrement the count for this residue
                freq[r] -= 1
                # Move to next potential MEX
                mex += 1
            else:
                # Cannot cover this mex, return it as the maximum achievable MEX
                return mex

    findSmallestInteger = find_smallest_integer
