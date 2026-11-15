# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/


class Solution:
    """1524. Number of Sub-arrays With Odd Sum

    Given an array of integers `arr`, return the number of subarrays with an
    odd sum.

    Since the answer can be very large, return it modulo 10**9 + 7.

    Constraints:

    * 1 <= arr.length <= 10**5
    * 1 <= arr[i] <= 100
    """

    def num_of_subarrays(self, arr: list[int]) -> int:
        """Count subarrays with odd sum using prefix parity counts.

        Track counts of even and odd prefix sums. For each new prefix, add
        the count of opposite-parity prefixes (which form odd-sum subarrays).
        """
        mod = 10**9 + 7
        # even starts at 1 for the empty prefix
        even = 1
        odd = 0
        ans = 0
        prefix = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                # current even pairs with previous odds
                ans += odd
                even += 1
            else:
                # current odd pairs with previous evens
                ans += even
                odd += 1
            ans %= mod
        return ans

    numOfSubarrays = num_of_subarrays
