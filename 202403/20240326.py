# https://leetcode.com/problems/first-missing-positive/


class Solution:
    """41. First Missing Positive

    Given an unsorted integer array `nums`. Return the *smallest positive integer* that
    is *not present* in `nums`.

    You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary
    space.

    """

    def first_missing_positive(self, nums: list[int]) -> int:
        n = len(nums)

        # Replace all negative numbers, zeros, and numbers out of range with n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Use the array to mark the presence of each number by negating the value at the corresponding index
        for i in range(n):
            if abs(nums[i]) > n:
                continue
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        # Iterate over the array and return the first index with a positive value, which corresponds to the first missing positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If all of them didn't return anything, this means the missing number is the last number
        return n + 1

    firstMissingPositive = first_missing_positive
