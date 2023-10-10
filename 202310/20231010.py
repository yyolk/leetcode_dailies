# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/


class Solution:
    """2009. Minimum Number of Operations to Make Array Continuous

    You are given an integer array `nums`. In one operation, you can replace **any**
    element in `nums` with **any** integer.

    `nums` is considered **continuous** if both of the following conditions are
    fulfilled:

    * All elements in `nums` are **unique**.

    * The difference between the **maximum** element and the **minimum** element in
    `nums` equals `nums.length - 1`.

    For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]`
    is **not continuous**.

    Return *the **minimum** number of operations to make* `nums`***continuous***.
    """

    def minOperations(self, nums: List[int]) -> int:
        ...
