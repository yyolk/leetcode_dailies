# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/


class Solution:
    """3512. Minimum Operations to Make Array Sum Divisible by K

    You are given an integer array nums and an integer k. You can perform the
    following operation any number of times:

    Select an index i and replace nums[i] with nums[i] - 1.
    Return the minimum number of operations required to make the sum of the array
    divisible by k.
    """
    def min_operations(self, nums: list[int], k: int) -> int:
        # Compute the total sum of the array
        total_sum = sum(nums)
        # The minimum operations needed is the remainder of total_sum divided by k
        # since each operation decreases the sum by 1, and we need sum % k == 0
        return total_sum % k

    minOperations = min_operations