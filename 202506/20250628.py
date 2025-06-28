# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/


class Solution:
    """2099. Find Subsequence of Length K With the Largest Sum

    You are given an integer array `nums` and an integer `k`. You want to find a
    **subsequence** of `nums` of length `k` that has the **largest** sum.

    Return***any** such subsequence as an integer array of length* `k`.

    A **subsequence** is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements."""

    def max_subsequence(self, nums: list[int], k: int) -> list[int]:
        # Create list of (value, index) pairs to track original positions
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        
        # Get the k largest elements with their indices
        largest_k = heapq.nlargest(k, indexed_nums, key=lambda x: x[0])
        
        # Sort them by their original index to maintain sequence order
        sorted_by_index = sorted(largest_k, key=lambda x: x[1])
        
        # Extract just the values in the sorted order
        result = [x[0] for x in sorted_by_index]
        
        return result

    maxSubsequence = max_subsequence
