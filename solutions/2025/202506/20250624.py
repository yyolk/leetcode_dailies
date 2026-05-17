# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/


class Solution:
    """2200. Find All K-Distant Indices in an Array

    You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A
    **k-distant index** is an index `i` of `nums` for which there exists at least one
    index `j` such that `|i - j| <= k` and `nums[j] == key`.

    Return *a list of all k-distant indices sorted in **increasing order***."""

    def find_k_distant_indices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        # Initialize difference array with size n+1 to handle range updates
        diff = [0] * (n + 1)

        # Step 1: Mark the influence range of each occurrence of key
        for j in range(n):
            if nums[j] == key:
                # For each j where nums[j] == key, index i is k-distant if i is in [j-k, j+k]
                # Adjust bounds to stay within array: [0, n-1]
                start = max(0, j - k)  # Leftmost index influenced by j
                end = min(n, j + k + 1)  # Rightmost index (exclusive) influenced by j
                diff[start] += 1  # Increment at start of range
                diff[end] -= 1  # Decrement at end+1 of range

        # Step 2: Compute prefix sum to determine which indices are k-distant
        result = []
        prefix = 0
        for i in range(n):
            prefix += diff[i]  # Running sum indicates coverage
            if prefix > 0:  # If >0, i is within k distance of some key
                result.append(i)

        return result

    findKDistantIndices = find_k_distant_indices
