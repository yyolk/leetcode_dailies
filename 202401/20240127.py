# https://leetcode.com/problems/k-inverse-pairs-array/


class Solution:
    """629. K Inverse Pairs Array

    For an integer array `nums`, an **inverse pair** is a pair of integers `[i, j]`
    where `0 <= i < j < nums.length` and `nums[i] > nums[j]`.

    Given two integers n and k, return the number of different arrays consist of numbers
    from `1` to `n` such that there are exactly `k` **inverse pairs**. Since the answer
    can be huge, return it **modulo** `109 + 7`.

    """

    def k_inverse_pairs(self, n: int, k: int) -> int: ...

    kInversePairs = k_inverse_pairs
