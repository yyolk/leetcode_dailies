# https://leetcode.com/problems/bitwise-xor-of-all-pairings/


class Solution:
    """2425. Bitwise XOR of All Pairings

    You are given two **0-indexed** arrays, `nums1` and `nums2`, consisting of non-
    negative integers. There exists another array, `nums3`, which contains the bitwise
    XOR of **all pairings** of integers between `nums1` and `nums2` (every integer in
    `nums1` is paired with every integer in `nums2` **exactly once**).

    Return *the **bitwise XOR** of all integers in* `nums3`."""

    def xor_all_nums(self, nums1: list[int], nums2: list[int]) -> int: ...

    xorAllNums = xor_all_nums
