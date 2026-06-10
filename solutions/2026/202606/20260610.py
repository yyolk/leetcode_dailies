# https://leetcode.com/problems/maximum-total-subarray-value-ii/


class Solution:
    """3691. Maximum Total Subarray Value II

    You are given an integer array `nums` of length `n` and an integer `k`.

    You must select **exactly** `k` **distinct** non-empty subarrays `nums[l..r]` of
    `nums`. Subarrays may overlap, but the exact same subarray (same `l` and `r`)
    **cannot** be chosen more than once.

    The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) -
    min(nums[l..r])`.

    The **total value** is the sum of the **values** of all chosen subarrays.

    Return the **maximum** possible total value you can achieve.

    Constraints:

    * `1 <= n == nums.length <= 5 * 10\u200b\u200b\u200b\u200b\u200b\u200b\u200b4`

    * `0 <= nums[i] <= 109`

    * `1 <= k <= min(105, n * (n + 1) / 2)`"""

    def max_total_value(self, nums: list[int], k: int) -> int: ...

    maxTotalValue = max_total_value
