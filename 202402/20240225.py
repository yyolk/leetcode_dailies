# https://leetcode.com/problems/greatest-common-divisor-traversal/


class Solution:
    """2709. Greatest Common Divisor Traversal

    You are given a **0-indexed** integer array `nums`, and you are allowed to
    **traverse** between its indices. You can traverse between index `i` and index `j`,
    `i != j`, if and only if `gcd(nums[i], nums[j]) > 1`, where `gcd` is the **greatest
    common divisor**.

    Your task is to determine if for **every pair** of indices `i` and `j` in nums,
    where `i < j`, there exists a **sequence of traversals** that can take us from `i`
    to `j`.

    Return `true` *if it is possible to traverse between all such pairs of indices,*
    *or* `false` *otherwise.*

    """

    def can_traverse_all_pairs(self, nums: list[int]) -> bool: ...

    canTraverseAllPairs = can_traverse_all_pairs
