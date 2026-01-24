# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array


class Solution:
    """1877. Minimize Maximum Pair Sum in Array

    The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum
    is the largest pair sum in a list of pairs.

    For example, if we have pairs (1,5), (2,3), and (4,4), the maximum
    pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

    Given an array nums of even length n, pair up the elements of nums
    into n / 2 pairs such that:

    Each element of nums is in exactly one pair, and
    The maximum pair sum is minimized.

    Return the minimized maximum pair sum after optimally pairing up
    the elements.
    """
    def min_pair_sum(self, nums: list[int]) -> int:
        # Sort the array to enable pairing smallest with largest
        nums.sort()
        # Initialize variable to track the maximum pair sum
        max_sum = 0
        # Get half the length for looping through pairs
        half = len(nums) // 2
        # Loop through the first half of the sorted array
        for i in range(half):
            # Calculate current pair sum: nums[i] + nums[-1-i]
            current = nums[i] + nums[len(nums) - 1 - i]
            # Update max_sum if current is larger
            if current > max_sum:
                max_sum = current
        # Return the minimized maximum pair sum
        return max_sum

    minPairSum = min_pair_sum