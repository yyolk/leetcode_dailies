# https://leetcode.com/problems/xor-after-range-multiplication-queries-i

class Solution:
    """3653. XOR After Range Multiplication Queries I
    
    You are given an integer array nums of length n and a 2D integer array
    queries of size q, where queries[i] = [li, ri, ki, vi]. For each query,
    you must apply the following operations in order: Set idx = li. While idx
    <= ri: Update: nums[idx] = (nums[idx] * vi) % (10**9 + 7) Set idx += ki.
    Return the bitwise XOR of all elements in nums after processing all
    queries.
    """
    def xor_after_queries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        for li, ri, ki, vi in queries:
            # process arithmetic progression for this query
            idx = li
            while idx <= ri:
                # multiply in place and apply modulo
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        # compute XOR of final array
        res = 0
        for num in nums:
            res ^= num
        return res

    xorAfterQueries = xor_after_queries