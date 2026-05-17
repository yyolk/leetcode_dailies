# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/


class Solution:
    """2441. Largest Positive Integer That Exists With Its Negative

    Given an integer array `nums` that **does not contain** any zeros, find **the
    largest positive** integer `k` such that `-k` also exists in the array.

    Return *the positive integer* `k`. If there is no such integer, return `-1`.

    """

    def find_max_k(self, nums: list[int]) -> int:
        # Make a set for faster lookup
        nums_set = set(nums)
        # Sort the list in reverse order
        nums.sort(reverse=True)
        for num in nums:
            # The first num we that also has its negative in the list is the largest k
            if -num in nums_set:
                return num
        # We didn't find any
        return -1

    findMaxK = find_max_k
