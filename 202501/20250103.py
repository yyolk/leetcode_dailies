# https://leetcode.com/problems/number-of-ways-to-split-array/


class Solution:
    """2270. Number of Ways to Split Array

    You are given a **0-indexed** integer array `nums` of length `n`.

    `nums` contains a **valid split** at index `i` if the following are true:

    * The sum of the first `i + 1` elements is **greater than or equal to** the sum of
    the last `n - i - 1` elements.

    * There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

    Return *the number of **valid splits** in* `nums`."""

    def ways_to_split_array(self, nums: list[int]) -> int: ...

    waysToSplitArray = ways_to_split_array
