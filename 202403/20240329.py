# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


class Solution:
    """2962. Count Subarrays Where Max Element Appears at Least K Times

    You are given an integer array `nums` and a **positive** integer `k`.

    Return *the number of subarrays where the **maximum** element of* `nums` *appears
    **at least*** `k` *times in that subarray.*

    A **subarray** is a contiguous sequence of elements within an array.

    """

    def count_subarrays(self, nums: list[int], k: int) -> int:
        # Find the maximum element in the list
        m = max(nums)
        # Initialize a frequency counter
        freq = Counter()
        # Initialize the answer and the starting index
        ans = ii = 0
        # Iterate through the list
        for x in nums:
            # Increment the frequency of the current element
            freq[x] += 1
            # While the maximum element appears at least k times
            while freq[m] >= k:
                # Decrement the frequency of the element at the starting index
                freq[nums[ii]] -= 1
                # Increment the starting index
                ii += 1
            # Increment the answer by the number of subarrays found so far
            ans += ii
        # Return the final answer
        return ans

    countSubarrays = count_subarrays
