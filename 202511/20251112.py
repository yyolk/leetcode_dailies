# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/


import math

class Solution:
    """2654. Minimum Number of Operations to Make All Array Elements Equal to 1

    You are given a 0-indexed array nums consisting of positive integers.
    You can do the following operation on the array any number of times:

    * Select an index i such that 0 <= i < n - 1 and replace either of
      nums[i] or nums[i+1] with their gcd value.

    Return the minimum number of operations to make all elements of nums
    equal to 1. If it is impossible, return -1.

    The gcd of two integers is the greatest common divisor of the two
    integers.
    """
    def min_operations(self, nums: list[int]) -> int:
        # Handle base case for empty array, though constraints imply n >= 1
        n = len(nums)
        if n == 0:
            return 0

        # Compute the GCD of the entire array
        overall_gcd = nums[0]
        for x in nums[1:]:
            overall_gcd = math.gcd(overall_gcd, x)
            # Early break if GCD reaches 1 for optimization
            if overall_gcd == 1:
                break

        # If overall GCD != 1, impossible to reach all 1s
        if overall_gcd != 1:
            return -1

        # Count the number of 1s in the array
        count_one = sum(1 for x in nums if x == 1)

        # If there are 1s, the min operations is n minus the count of 1s
        if count_one > 0:
            return n - count_one

        # Build sparse table for O(1) range GCD queries
        logn = int(math.log2(n)) + 1
        st = [[0] * n for _ in range(logn)]
        for i in range(n):
            st[0][i] = nums[i]
        for k in range(1, logn):
            for i in range(n - (1 << k) + 1):
                st[k][i] = math.gcd(st[k-1][i], st[k-1][i + (1 << (k-1))])

        # Query function for GCD from left to right inclusive
        def get_gcd(left: int, right: int) -> int:
            length = right - left + 1
            k = int(math.log2(length))
            return math.gcd(st[k][left], st[k][right - (1 << k) + 1])

        # Binary search to find the minimal subarray length l where some sub has GCD 1
        low = 2
        high = n
        min_l = n  # Initialize to maximum possible
        while low <= high:
            mid = (low + high) // 2
            found = False
            # Check each possible subarray of length mid
            for i in range(n - mid + 1):
                if get_gcd(i, i + mid - 1) == 1:
                    found = True
                    break
            if found:
                min_l = mid
                high = mid - 1
            else:
                low = mid + 1

        # Calculate operations: n + min_l - 2
        return n + min_l - 2

    minOperations = min_operations