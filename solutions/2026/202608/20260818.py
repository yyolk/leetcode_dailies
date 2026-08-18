# https://leetcode.com/problems/find-the-largest-almost-missing-integer/


class Solution:
    """3471. Find the Largest Almost Missing Integer

    You are given an integer array `nums` and an integer `k`.

    An integer `x` is **almost missing** from `nums` if `x` appears in *exactly* one
    subarray of size `k` within `nums`.

    Return the **largest** **almost missing** integer from `nums`. If no such integer
    exists, return `-1`.

    A **subarray** is a contiguous sequence of elements within an array.

    Constraints:

    * `1 <= nums.length <= 50`

    * `0 <= nums[i] <= 50`

    * `1 <= k <= nums.length`"""

    def largest_integer(self, nums: list[int], k: int) -> int:
        """Return the largest integer appearing in exactly one length-k subarray."""
        window_count: dict[int, int] = {}
        for start in range(len(nums) - k + 1):
            for value in set(nums[start : start + k]):
                window_count[value] = window_count.get(value, 0) + 1

        best = -1
        for value, count in window_count.items():
            if count == 1:
                best = max(best, value)
        return best

    largestInteger = largest_integer
