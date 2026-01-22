# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i


class Solution:
    """3507. Minimum Pair Removal to Sort Array I

    Given an array nums, you can perform the following operation any number
    of times:

    Select the adjacent pair with the minimum sum in nums. If multiple such
    pairs exist, choose the leftmost one.
    Replace the pair with their sum.
    Return the minimum number of operations needed to make the array
    non-decreasing.

    An array is said to be non-decreasing if each element is greater than
    or equal to its previous element (if it exists).
    """
    def minimum_pair_removal(self, nums: list[int]) -> int:
        # Copy the list to avoid modifying the original
        nums = nums[:]
        ops = 0
        while len(nums) > 1:
            # Check if the array is non-decreasing
            is_non_dec = True
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    is_non_dec = False
                    break
            if is_non_dec:
                return ops
            # Find the leftmost pair with the minimum sum
            min_sum = float('inf')
            min_i = -1
            for i in range(len(nums) - 1):
                cur_sum = nums[i] + nums[i + 1]
                # Update if smaller sum or same sum but leftier
                if cur_sum < min_sum or (cur_sum == min_sum and i < min_i):
                    min_sum = cur_sum
                    min_i = i
            # Merge the pair into their sum
            new_v = nums[min_i] + nums[min_i + 1]
            nums = nums[:min_i] + [new_v] + nums[min_i + 2 :]
            ops += 1
        # If reduced to one element, it's always non-decreasing
        return ops

    minimumPairRemoval = minimum_pair_removal