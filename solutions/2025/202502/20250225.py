# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
MOD = 1000000007  # 10^9 + 7


class Solution:
    """1524. Number of Sub-arrays With Odd Sum

    Given an array of integers `arr`, return *the number of subarrays with an **odd**
    sum*.

    Since the answer can be very large, return it modulo `109 + 7`."""

    def num_of_subarrays(self, arr: list[int]) -> int:
        # Include prefix sum of 0
        count_even = 1
        count_odd = 0
        total = 0
        current_prefix = 0
        for num in arr:
            current_prefix = (current_prefix + num) % 2
            # Current prefix sum is odd
            if current_prefix == 1:
                total = (total + count_even) % MOD
            # Current prefix sum is even
            else:
                total = (total + count_odd) % MOD
            # Update counts
            if current_prefix == 0:
                count_even += 1
            else:
                count_odd += 1
        return total

    numOfSubarrays = num_of_subarrays
