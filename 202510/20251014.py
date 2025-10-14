# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/


class Solution:
    """3349. Adjacent Increasing Subarrays Detection I

    Given an array `nums` of `n` integers and an integer `k`, determine whether there
    exist **two** **adjacent** subarrays of length `k` such that both subarrays are
    **strictly** **increasing**. Specifically, check if there are **two** subarrays
    starting at indices `a` and `b` (`a < b`), where:

    * Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly
    increasing**.

    * The subarrays must be **adjacent**, meaning `b = a + k`.

    Return `true` if it is *possible* to find **two** such subarrays, and `false`
    otherwise."""

    def has_increasing_subarrays(self, nums: list[int], k: int) -> bool: ...

    hasIncreasingSubarrays = has_increasing_subarrays
