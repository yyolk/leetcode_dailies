# https://leetcode.com/problems/smallest-stable-index-ii/


class Solution:
    """3904. Smallest Stable Index II

    You are given an integer array `nums` of length `n` and an integer `k`.

    For each index `i`, define its **instability score** as `max(nums[0..i]) -
    min(nums[i..n - 1])`.

    In other words:

    * `max(nums[0..i])` is the **largest** value among the elements from index 0 to
    index `i`.

    * `min(nums[i..n - 1])` is the **smallest** value among the elements from index `i`
    to index `n - 1`.

    An index `i` is called **stable** if its instability score is **less than or equal
    to** `k`.

    Return the **smallest** stable index. If no such index exists, return -1.

    Constraints:

    * `1 <= nums.length <= 105`

    * `0 <= nums[i] <= 109`

    * `0 <= k <= 109`
    """

    def first_stable_index(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Precompute suffix minima: suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Scan left-to-right with running prefix max
        prefix_max = 0
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i
        return -1

    firstStableIndex = first_stable_index
