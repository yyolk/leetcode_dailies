# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

import math


class Solution:
    """1979. Find Greatest Common Divisor of Array

    Given an integer array nums, return the greatest common divisor of the
    smallest number and largest number in nums.

    The greatest common divisor of two numbers is the largest positive integer
    that evenly divides both numbers.

    Constraints:
    * 2 <= nums.length <= 1000
    * 1 <= nums[i] <= 1000"""

    def find_g_c_d(self, nums: list[int]) -> int:
        # Find smallest and largest values (two passes are fine given n<=1000)
        smallest = min(nums)
        largest = max(nums)
        # Compute GCD via built-in Euclidean algorithm (optimal speed)
        return math.gcd(smallest, largest)

    findGCD = find_g_c_d
