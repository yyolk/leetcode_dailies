# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/


class Solution:
    """2302. Count Subarrays With Score Less Than K

    The **score** of an array is defined as the **product** of its sum and its length.

    * For example, the score of `[1, 2, 3, 4, 5]` is `(1 + 2 + 3 + 4 + 5) * 5 = 75`.

    Given a positive integer array `nums` and an integer `k`, return *the **number of
    non-empty subarrays** of* `nums` *whose score is **strictly less** than* `k`.

    A **subarray** is a contiguous sequence of elements within an array."""

    def count_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        result = 0
        left = 0
        current_sum = 0
        
        for right in range(n):
            # Add the current element to the window's sum
            current_sum += nums[right]
            
            # Shrink the window from the left while the score is >= k
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            # Count the number of valid subarrays ending at 'right'
            if left <= right:
                result += right - left + 1
        
        return result

    countSubarrays = count_subarrays
