# https://leetcode.com/problems/rearrange-array-elements-by-sign/


class Solution:
    """2149. Rearrange Array Elements by Sign

    You are given a **0-indexed** integer array `nums` of **even** length consisting of
    an **equal** number of positive and negative integers.

    You should **rearrange** the elements of `nums` such that the modified array follows
    the given conditions:

    1. Every **consecutive pair** of integers have **opposite signs**.

    2. For all integers with the same sign, the **order** in which they were present in
    `nums` is **preserved**.

    3. The rearranged array begins with a positive integer.

    Return *the modified array after rearranging the elements to satisfy the
    aforementioned conditions*.

    """

    def rearrange_array(self, nums: list[int]) -> list[int]: ...

    rearrangeArray = rearrange_array
