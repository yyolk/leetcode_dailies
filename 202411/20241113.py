# https://leetcode.com/problems/count-the-number-of-fair-pairs/


class Solution:
    """2563. Count the Number of Fair Pairs

    Given a **0\\-indexed** integer array `nums` of size `n` and two integers `lower` and
    `upper`, return *the number of fair pairs*.

    A pair `(i, j)` is **fair** if:

    * `0 <= i < j < n`, and

    * `lower <= nums[i] + nums[j] <= upper`

    """

    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int: ...

    countFairPairs = count_fair_pairs
