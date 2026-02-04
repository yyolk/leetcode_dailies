# https://leetcode.com/problems/trionic-array-ii


class Solution:
    """3640. Trionic Array II
    
    You are given an integer array nums of length n.
    A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n)
    for which there exist indices l < p < q < r such that:
    
    * nums[l...p] is strictly increasing,
    * nums[p...q] is strictly decreasing,
    * nums[q...r] is strictly increasing.
    
    Return the maximum sum of any trionic subarray in nums.
    """
    def max_sum_trionic(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0  # No possible trionic subarray
        
        INF = 10**18 + 5
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Maximal increasing ending at i
        left_start = [0] * n
        for i in range(n):
            if i > 0 and nums[i - 1] < nums[i]:
                left_start[i] = left_start[i - 1]
            else:
                left_start[i] = i
        
        # Maximal increasing starting at i
        right_end = [0] * n
        right_end[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_end[i] = right_end[i + 1]
            else:
                right_end[i] = i
        
        # Max sum of left increasing part ending at p (at least 2 elements)
        max_left = [-INF] * n
        cur_min = INF
        prev_lstart = -1
        for i in range(n):
            lstart = left_start[i]
            if lstart != prev_lstart:
                prev_lstart = lstart
                cur_min = prefix[lstart]
            # Set using min over prefixes up to previous (exclude single)
            if lstart < i:
                max_left[i] = prefix[i + 1] - cur_min
            # Add current for next positions
            cur_min = min(cur_min, prefix[i])
        
        # Max sum of right increasing part starting at q (at least 2 elements)
        max_right = [-INF] * n
        cur_max = -INF
        prev_rend = -1
        for i in range(n - 1, -1, -1):
            rend = right_end[i]
            if rend != prev_rend:
                prev_rend = rend
                cur_max = prefix[rend + 1]
            # Set using max over prefixes from next (exclude single)
            if right_end[i] > i:
                max_right[i] = cur_max - prefix[i]
            # Add current for previous positions
            cur_max = max(cur_max, prefix[i + 1])
        
        # Maximal decreasing ending at i
        dec_start = [0] * n
        for i in range(n):
            if i > 0 and nums[i - 1] > nums[i]:
                dec_start[i] = dec_start[i - 1]
            else:
                dec_start[i] = i
        
        # Precompute contribution of left part for each possible p
        val = [-INF] * n
        for p in range(n):
            if max_left[p] != -INF:
                val[p] = max_left[p] - prefix[p + 1]
        
        # Scan decreasing runs to find best p for each q
        ans = -INF
        cur_max_val = -INF
        prev_dstart = -1
        for i in range(n):
            dstart = dec_start[i]
            if dstart != prev_dstart:
                prev_dstart = dstart
                cur_max_val = -INF
            # Add new possible p = i-1 when run continues
            if i > 0 and dec_start[i] == dec_start[i - 1]:
                cur_max_val = max(cur_max_val, val[i - 1])
            # Valid middle (>=2) and right (>=2) and left exists
            if dstart < i and max_right[i] != -INF and cur_max_val != -INF:
                this_sum = cur_max_val + prefix[i] + max_right[i]
                ans = max(ans, this_sum)
        
        return ans

    maxSumTrionic = max_sum_trionic