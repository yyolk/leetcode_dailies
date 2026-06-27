# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/


class Solution:
    """3020. Find the Maximum Number of Elements in Subset

    You are given an array of **positive** integers `nums`.

    You need to select a subset of `nums` which satisfies the following condition:

    * You can place the selected elements in a **0-indexed** array such that it follows
    the pattern: `[x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x]` (**Note** that `k`
    can be be any **non-negative** power of `2`). For example, `[2, 4, 16, 4, 2]` and
    `[3, 9, 3]` follow the pattern while `[2, 4, 8, 4, 2]` does not.

    Return *the **maximum** number of elements in a subset that satisfies these
    conditions.*

    Constraints:

    * `2 <= nums.length <= 105`

    * `1 <= nums[i] <= 109`"""

    def maximum_length(self, nums: list[int]) -> int: ...

    maximumLength = maximum_length
