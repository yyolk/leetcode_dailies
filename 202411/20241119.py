# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


class Solution:
    """2461. Maximum Sum of Distinct Subarrays With Length K

    You are given an integer array `nums` and an integer `k`. Find the maximum subarray
    sum of all the subarrays of `nums` that meet the following conditions:

    * The length of the subarray is `k`, and

    * All the elements of the subarray are **distinct**.

    Return *the maximum subarray sum of all the subarrays that meet the conditions**.*
    If no subarray meets the conditions, return `0`.

    *A **subarray** is a contiguous non\\-empty sequence of elements within an array.*

    """

    def maximum_subarray_sum(self, nums: list[int], k: int) -> int: ...

    maximumSubarraySum = maximum_subarray_sum
