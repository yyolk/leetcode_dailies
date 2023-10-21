# https://leetcode.com/problems/constrained-subsequence-sum/


class Solution:
    """1425. Constrained Subsequence Sum

    Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-
    empty** subsequence of that array such that for every two **consecutive** integers
    in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <=
    k` is satisfied.

    A *subsequence* of an array is obtained by deleting some number of elements (can be
    zero) from the array, leaving the remaining elements in their original order.
    """

    def constrained_subset_sum(self, nums: List[int], k: int) -> int:
        ...

    constrainedSubsetSum = constrained_subset_sum
