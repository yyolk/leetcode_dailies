# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/


class Solution:
    """632. Smallest Range Covering Elements from K Lists

    You have `k` lists of sorted integers in **non\\-decreasing order**. Find the
    **smallest** range that includes at least one number from each of the `k` lists.

    We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c`
    **or** `a < c` if `b - a == d - c`.

    """

    def smallest_range(self, nums: list[list[int]]) -> list[int]: ...

    smallestRange = smallest_range
