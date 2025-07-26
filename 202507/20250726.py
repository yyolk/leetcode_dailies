# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/


class Solution:
    """3480. Maximize Subarrays After Removing One Conflicting Pair

    You are given an integer `n` which represents an array `nums` containing the numbers
    from 1 to `n` in order. Additionally, you are given a 2D array `conflicting_pairs`,
    where `conflicting_pairs[i] = [a, b]` indicates that `a` and `b` form a conflicting
    pair.

    Remove **exactly** one element from `conflicting_pairs`. Afterward, count the number
    of non-empty subarrays of `nums` which do not contain both `a` and `b` for any
    remaining conflicting pair `[a, b]`.

    Return the **maximum** number of subarrays possible after removing **exactly** one
    conflicting pair."""

    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int: ...

    maxSubarrays = max_subarrays
