# https://leetcode.com/problems/special-array-ii/


class Solution:
    """3152. Special Array II

    An array is considered **special** if every pair of its adjacent elements contains
    two numbers with different parity.

    You are given an array of integer `nums` and a 2D integer matrix `queries`, where
    for `queries[i] = [fromi, toi]` your task is to check that subarray
    `nums[fromi..toi]` is **special** or not.

    Return an array of booleans `answer` such that `answer[i]` is `true` if
    `nums[fromi..toi]` is special."""

    def is_array_special(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[bool]: ...

    isArraySpecial = is_array_special
