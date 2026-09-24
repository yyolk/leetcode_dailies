# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/


class Solution:
    """3550. Smallest Index With Digit Sum Equal to Index

    You are given an integer array `nums`.

    Return the **smallest** index `i` such that the sum of the digits of
    `nums[i]` is equal to `i`.

    If no such index exists, return `-1`.

    Constraints:

    * `1 <= nums.length <= 100`

    * `0 <= nums[i] <= 1000`
    """

    def smallest_index(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0
            # Sum decimal digits; nums[i] <= 1000 so at most four digits.
            while num:
                digit_sum += num % 10
                num //= 10
            if digit_sum == i:
                return i
        return -1

    smallestIndex = smallest_index
