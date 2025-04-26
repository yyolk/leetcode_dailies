# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution:
    """2444. Count Subarrays With Fixed Bounds

    You are given an integer array `nums` and two integers `min_k` and `max_k`.

    A **fixed-bound subarray** of `nums` is a subarray that satisfies the following
    conditions:

    * The **minimum** value in the subarray is equal to `min_k`.

    * The **maximum** value in the subarray is equal to `max_k`.

    Return *the **number** of fixed-bound subarrays*.

    A **subarray** is a **contiguous** part of an array."""

    def count_subarrays(self, nums: list[int], min_k: int, max_k: int) -> int:
        # Initialize variables to track positions and count
        bad_pos = -1      # Last position where element is outside [min_k, max_k]
        minK_pos = -1     # Last position where min_k was seen
        maxK_pos = -1     # Last position where max_k was seen
        total_count = 0   # Total number of valid subarrays
        
        # Iterate through the array
        for i in range(len(nums)):
            # Check if current element is outside the range [min_k, max_k]
            if nums[i] < min_k or nums[i] > max_k:
                bad_pos = i
                minK_pos = -1
                maxK_pos = -1
            else:
                # Update positions if current element is min_k or max_k
                if nums[i] == min_k:
                    minK_pos = i
                if nums[i] == max_k:
                    maxK_pos = i
                # If both min_k and max_k have been seen in current segment
                if minK_pos != -1 and maxK_pos != -1:
                    # Number of valid subarrays ending at i
                    total_count += min(minK_pos, maxK_pos) - bad_pos
        
        return total_count

    countSubarrays = count_subarrays
