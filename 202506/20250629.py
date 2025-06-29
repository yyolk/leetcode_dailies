# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
import bisect

MOD = 1_000_000_007


class Solution:
    """1498. Number of Subsequences That Satisfy the Given Sum Condition

    You are given an array of integers `nums` and an integer `target`.

    Return *the number of **non-empty** subsequences of* `nums` *such that the sum of
    the minimum and maximum element on it is less or equal to* `target`. Since the
    answer may be too large, return it **modulo** `109 + 7`."""

    def num_subseq(self, nums: list[int], target: int) -> int:        
        # Sort the array in ascending order
        nums.sort()
        n = len(nums)
        
        # Precompute powers of 2 modulo MOD
        pow2 = [1]
        for _ in range(n):
            pow2.append((pow2[-1] * 2) % MOD)
        
        total = 0
        # For each index i as potential minimum
        for i in range(n):
            # Find the largest j such that nums[i] + nums[j] <= target
            j = bisect.bisect_right(nums, target - nums[i]) - 1
            if j >= i:
                # Add the number of valid subsequences where nums[i] is min
                # and max is <= nums[j]
                total = (total + pow2[j - i]) % MOD
        
        return total

    numSubseq = num_subseq
