# https://leetcode.com/problems/count-nice-pairs-in-an-array/


class Solution:
    """1814. Count Nice Pairs in an Array

    You are given an array `nums` that consists of non-negative integers. Let us define
    `rev(x)` as the reverse of the non-negative integer `x`. For example, `rev(123) =
    321`, and `rev(120) = 21`. A pair of indices `(i, j)` is **nice** if it satisfies
    all of the following conditions:

    * `0 <= i < j < nums.length`

    * `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`

    Return *the number of nice pairs of indices*. Since that number can be too large,
    return it **modulo** `109 + 7`.
    """

    def count_nice_pairs(self, nums: List[int]) -> int:
        ...

    countNicePairs = count_nice_pairs
