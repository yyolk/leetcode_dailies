# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/


class Solution:
    """3254. Find the Power of K-Size Subarrays I

    You are given an array of integers `nums` of length `n` and a *positive* integer
    `k`.

    The **power** of an array is defined as:

    * Its **maximum** element if *all* of its elements are **consecutive** and
    **sorted** in **ascending** order.

    * \\-1 otherwise.

    You need to find the **power** of all subarrays of `nums` of size `k`.

    Return an integer array `results` of size `n - k + 1`, where `results[i]` is the
    *power* of `nums[i..(i + k - 1)]`.

    """

    def results_array(self, nums: list[int], k: int) -> list[int]: ...

    resultsArray = results_array
