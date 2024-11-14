# https://leetcode.com/problems/count-the-number-of-fair-pairs/
from bisect import bisect_left, bisect_right


class Solution:
    """2563. Count the Number of Fair Pairs

    Given a **0\\-indexed** integer array `nums` of size `n` and two integers `lower` and
    `upper`, return *the number of fair pairs*.

    A pair `(i, j)` is **fair** if:

    * `0 <= i < j < n`, and

    * `lower <= nums[i] + nums[j] <= upper`

    """

    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Sort the array for binary search
        nums.sort()
        n = len(nums)
        count = 0

        # Iterate over each number
        for i in range(n):
            # Find the index where the sum would be at least `lower`
            left = bisect_left(nums, lower - nums[i], i + 1)
            # Find the index where the sum would exceed `upper`
            right = bisect_right(nums, upper - nums[i], i + 1)

            # Add the number of valid pairs for this number
            count += right - left

        return count

    countFairPairs = count_fair_pairs
