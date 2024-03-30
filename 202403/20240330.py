# https://leetcode.com/problems/subarrays-with-k-different-integers/


class Solution:
    """992. Subarrays with K Different Integers

    Given an integer array `nums` and an integer `k`, return *the number of **good
    subarrays** of* `nums`.

    A **good array** is an array where the number of different integers in that array is
    exactly `k`.

    * For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.

    A **subarray** is a **contiguous** part of an array.

    """
    def at_most_k_distinct(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        distinct = 0
        result = 0

        for right in range(len(nums)):
            if count[nums[right]] == 0:
                distinct += 1
            count[nums[right]] += 1

            while distinct > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    distinct -= 1
                left += 1

            result += right - left + 1

        return result

    def subarrays_with_k_distinct(self, nums: list[int], k: int) -> int:
        return self.at_most_k_distinct(nums, k) - self.at_most_k_distinct(nums, k - 1)

    subarraysWithKDistinct = subarrays_with_k_distinct
