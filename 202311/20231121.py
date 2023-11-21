# https://leetcode.com/problems/count-nice-pairs-in-an-array/
from collections import Counter


MOD = 10**9 + 7


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

    def count_nice_pairs(self, nums: list[int]) -> int:
        """Count and Return the number of nice pairs.

        Args:
            nums: Input list of non-negative integers to count nice pairs of from
                opposite sides to determine if their sum matches the reverse of either.

        Returns:
            The number of nice pairs of indices MOD 10^9 + 7.
        """
        # Calculate the complement of each number.
        complement_nums = [i - int(str(i)[::-1]) for i in nums]

        nice_pairs_count = 0

        # Count occurrences of each complement using Counter.
        for num in Counter(complement_nums).values():
            # Calculate the number of pairs that can be formed with 'num' occurrences.
            nice_pairs_count += num * (num - 1) // 2
        return nice_pairs_count % MOD

    countNicePairs = count_nice_pairs
