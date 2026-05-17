# https://leetcode.com/problems/greatest-common-divisor-traversal/
from math import gcd


class Solution:
    """2709. Greatest Common Divisor Traversal

    You are given a **0-indexed** integer array `nums`, and you are allowed to
    **traverse** between its indices. You can traverse between index `i` and index `j`,
    `i != j`, if and only if `gcd(nums[i], nums[j]) > 1`, where `gcd` is the **greatest
    common divisor**.

    Your task is to determine if for **every pair** of indices `i` and `j` in nums,
    where `i < j`, there exists a **sequence of traversals** that can take us from `i`
    to `j`.

    Return `true` *if it is possible to traverse between all such pairs of indices,*
    *or* `false` *otherwise.*

    """

    def can_traverse_all_pairs(self, nums: list[int]) -> bool:
        # Check for the edge case with only one element
        if len(nums) == 1:
            return True

        # Check for the presence of '1' in nums
        if 1 in nums:
            return False

        # Remove duplicates and sort nums in descending order
        nums = sorted(set(nums), reverse=True)
        n = len(nums)

        # Check if n is still 1 after removing duplicates
        if n == 1:
            return True

        # Iterate through the pairs of indices
        for i in range(n - 1):
            for j in range(i + 1, n):
                # If GCD(nums[i], nums[j]) - 1 is non-zero, update nums[j] and break
                if gcd(nums[i], nums[j]) - 1:
                    nums[j] *= nums[i]
                    break
            else:
                # If no match is found, there is no traversal sequence
                return False

        # If all pairs have traversal sequences, return True
        return True

    canTraverseAllPairs = can_traverse_all_pairs
