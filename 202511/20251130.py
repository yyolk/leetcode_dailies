# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List

class Solution:
    """1590. Make Sum Divisible by P

    Given an array of positive integers nums, remove the smallest subarray
    (possibly empty) such that the sum of the remaining elements is divisible
    by p. It is not allowed to remove the whole array.

    Return the length of the smallest subarray that you need to remove, or -1
    if it's impossible.

    A subarray is defined as a contiguous block of elements in the array.
    """
    def min_subarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        # Compute total sum and its modulo p
        total = sum(nums)
        r = total % p
        # If total sum already divisible by p, remove empty subarray
        if r == 0:
            return 0
        # Map to track last index for each prefix sum modulo p
        seen = {0: -1}
        # Current prefix sum modulo p
        curr = 0
        # Track minimum subarray length (init to full length)
        min_len = n
        for i in range(n):
            # Accumulate prefix sum modulo p
            curr = (curr + nums[i]) % p
            # Target prefix modulo for subarray sum % p == r
            target = (curr - r + p) % p
            if target in seen:
                # Length of candidate subarray ending at i
                length = i - seen[target]
                # Update min if shorter than current min
                if length < min_len:
                    min_len = length
            # Update last seen index for current prefix modulo
            seen[curr] = i
        # If only full array works, impossible (can't remove whole)
        return -1 if min_len == n else min_len

    minSubarray = min_subarray