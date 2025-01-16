# https://leetcode.com/problems/bitwise-xor-of-all-pairings/


class Solution:
    """2425. Bitwise XOR of All Pairings

    You are given two **0-indexed** arrays, `nums1` and `nums2`, consisting of non-
    negative integers. There exists another array, `nums3`, which contains the bitwise
    XOR of **all pairings** of integers between `nums1` and `nums2` (every integer in
    `nums1` is paired with every integer in `nums2` **exactly once**).

    Return *the **bitwise XOR** of all integers in* `nums3`."""

    def xor_all_nums(self, nums1: list[int], nums2: list[int]) -> int:
        xor1 = 0
        xor2 = 0
        
        # XOR all numbers in nums1
        for num in nums1:
            xor1 ^= num
        
        # XOR all numbers in nums2
        for num in nums2:
            xor2 ^= num
        
        result = 0
        # If nums2 has an odd length, every number in nums1 will contribute to the result
        if len(nums2) % 2 == 1:
            result ^= xor1
        # If nums1 has an odd length, every number in nums2 will contribute to the result
        if len(nums1) % 2 == 1:
            result ^= xor2
        
        return result

    xorAllNums = xor_all_nums
