# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/


class Solution:
    """1526. Minimum Number of Increments on Subarrays to Form a Target Array

    You are given an integer array `target`. You have an integer array `initial` of the
    same size as `target` with all elements initially zeros.

    In one operation you can choose **any** subarray from `initial` and increment each
    value by one.

    Return *the minimum number of operations to form a* `target` *array from* `initial`.

    The test cases are generated so that the answer fits in a 32-bit integer."""

    def min_number_operations(self, target: list[int]) -> int: ...

    minNumberOperations = min_number_operations
