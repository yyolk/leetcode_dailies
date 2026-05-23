# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    """1752. Check if Array Is Sorted and Rotated

    Given an array nums, return true if the array was originally sorted in non-
    decreasing order, then rotated some number of positions (including zero).
    Otherwise, return false. There may be duplicates in the original array.
    Note: An array A rotated by x positions results in an array B of the same
    length such that B[i] == A[(i+x) % A.length] for every valid index i.
    """
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        drops = 0
        # count decreases between consecutive elements (linear part)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                drops += 1
        # add wrap-around decrease from end to start (circular rotation point)
        if nums and nums[-1] > nums[0]:
            drops += 1
        # at most one drop allowed for any valid sorted rotated array
        return drops <= 1

    check = check