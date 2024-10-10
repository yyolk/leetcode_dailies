# https://leetcode.com/problems/maximum-width-ramp/


class Solution:
    """962. Maximum Width Ramp

    A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and
    `nums[i] <= nums[j]`. The **width** of such a ramp is `j - i`.

    Given an integer array `nums`, return *the maximum width of a **ramp** in* `nums`.
    If there is no **ramp** in `nums`, return `0`.

    """

    def max_width_ramp(self, nums: list[int]) -> int: ...

    maxWidthRamp = max_width_ramp
