# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/


class Solution:
    """2958. Length of Longest Subarray With at Most K Frequency

    You are given an integer array `nums` and an integer `k`.

    The **frequency** of an element `x` is the number of times it occurs in an array.

    An array is called **good** if the frequency of each element in this array is **less
    than or equal** to `k`.

    Return *the length of the **longest** **good** subarray of* `nums`*.*

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    """

    def max_subarray_length(self, nums: list[int], k: int) -> int: ...

    maxSubarrayLength = max_subarray_length
