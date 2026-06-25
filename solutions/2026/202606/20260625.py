# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution:
    """3737. Count Subarrays With Majority Element I

You are given an integer array nums and an integer target. Return the number of
subarrays of nums in which target is the majority element. The majority element
of a subarray is the element that appears strictly more than half of the times in
that subarray.

Constraints:
* 1 <= nums.length <= 1000
* 1 <= nums[i] <= 10**9
* 1 <= target <= 10**9
"""
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            # incremental count of target for subarrays starting at i
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1
                length = j - i + 1
                # target is majority if strictly > half the length
                if count > length // 2:
                    ans += 1
        return ans

    countMajoritySubarrays = count_majority_subarrays