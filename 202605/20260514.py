# https://leetcode.com/problems/check-if-array-is-good/


class Solution:
    """2784. Check if Array is Good

    You are given an integer array nums. We consider an array good if it is a
    permutation of an array base[n]. base[n] = [1, 2, ..., n - 1, n, n] (in
    other words, it is an array of length n + 1 which contains 1 to n - 1
    exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and
    base[3] = [1, 2, 3, 3]. Return true if the given array is good, otherwise
    return false. Note: A permutation of integers represents an arrangement of
    these numbers.
    """

    def is_good(self, nums: list[int]) -> bool:
        m = len(nums)
        if m < 2:
            return False
        n = m - 1
        # sort nums in-place to allow O(1) extra space verification
        nums.sort()
        # positions 0 to n-2 must contain 1 to n-1 exactly
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        # last two positions must both be n
        return nums[-2] == n and nums[-1] == n

    isGood = is_good
