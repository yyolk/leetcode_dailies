# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/


class Solution:
    """2200. Find All K-Distant Indices in an Array

    You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A
    **k-distant index** is an index `i` of `nums` for which there exists at least one
    index `j` such that `|i - j| <= k` and `nums[j] == key`.

    Return *a list of all k-distant indices sorted in **increasing order***."""

    def find_k_distant_indices(
        self, nums: list[int], key: int, k: int
    ) -> list[int]: ...

    findKDistantIndices = find_k_distant_indices
