# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/


class Solution:
    """2044. Count Number of Maximum Bitwise-OR Subsets

    Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a
    subset of `nums` and return *the **number of different non\\-empty subsets** with the
    maximum bitwise OR*.

    An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by
    deleting some (possibly zero) elements of `b`. Two subsets are considered
    **different** if the indices of the elements chosen are different.

    The bitwise OR of an array `a` is equal to `a[0] OR a[1] OR ... OR a[a.length - 1]`
    (**0\\-indexed**).

    """

    def count_max_or_subsets(self, nums: list[int]) -> int: ...

    countMaxOrSubsets = count_max_or_subsets
