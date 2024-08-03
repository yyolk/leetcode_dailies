# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/


class Solution:
    """1460. Make Two Arrays Equal by Reversing Subarrays

    You are given two integer arrays of equal length `target` and `arr`. In one step,
    you can select any **non\\-empty subarray** of `arr` and reverse it. You are allowed
    to make any number of steps.

    Return `true` *if you can make* `arr` *equal to* `target`*or* `false` *otherwise*.

    """

    def can_be_equal(self, target: list[int], arr: list[int]) -> bool: ...

    canBeEqual = can_be_equal
