# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

from math import gcd


class Solution:
    """3867. Sum of GCD of Formed Pairs

    You are given an integer array nums of length n. Construct an array
    prefixGcd where for each index i: Let mxi = max(nums[0], nums[1], ...,
    nums[i]). prefixGcd[i] = gcd(nums[i], mxi). After constructing prefixGcd:
    Sort prefixGcd in non-decreasing order. Form pairs by taking the smallest
    unpaired element and the largest unpaired element. Repeat this process
    until no more pairs can be formed. For each formed pair, compute the gcd
    of the two elements. If n is odd, the middle element in the prefixGcd
    array remains unpaired and should be ignored. Return an integer denoting
    the sum of the GCD values of all formed pairs. The term gcd(a, b)
    denotes the greatest common divisor of a and b.
    """

    def gcd_sum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        prefix_gcd = [0] * n
        running_max = 0
        for i in range(n):
            running_max = max(running_max, nums[i])
            # prefixGcd[i] = gcd(nums[i], max so far)
            prefix_gcd[i] = gcd(nums[i], running_max)
        # sort in non-decreasing order
        prefix_gcd.sort()
        total = 0
        # pair smallest with largest, next smallest with next largest, etc.
        for i in range(n // 2):
            # gcd of pair (prefix_gcd[i], prefix_gcd[n-1-i])
            total += gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
        return total

    gcdSum = gcd_sum
