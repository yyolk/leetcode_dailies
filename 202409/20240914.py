# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/


class Solution:
    """2419. Longest Subarray With Maximum Bitwise AND

    You are given an integer array `nums` of size `n`.

    Consider a **non\\-empty** subarray from `nums` that has the **maximum** possible
    **bitwise AND**.

    * In other words, let `k` be the maximum value of the bitwise AND of **any**
    subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be
    considered.

    Return *the length of the **longest** such subarray*.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A **subarray** is a contiguous sequence of elements within an array.

    """

    def longest_subarray(self, nums: list[int]) -> int:
        # Find the maximum number in nums, which sets an upper bound for max bitwise AND
        max_num = max(nums)
        
        # If nums is empty, return 0
        if not max_num:
            return 0
        
        # Group consecutive equal elements in nums
        grouped_nums = groupby(nums)
        
        # Find the longest group where the number equals max_num
        # This works because max bitwise AND will always be max_num if all elements in subarray are max_num
        return max(len(list(group)) for num, group in grouped_nums if num == max_num)

    longestSubarray = longest_subarray
