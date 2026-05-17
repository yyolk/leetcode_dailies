# https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    """523. Continuous Subarray Sum

    Given an integer array nums and an integer k, return `true` *if* `nums` *has a
    **good subarray** or* `false` *otherwise*.

    A **good subarray** is a subarray where:

    * its length is **at least two**, and

    * the sum of the elements of the subarray is a multiple of `k`.

    **Note** that:

    * A **subarray** is a contiguous part of the array.

    * An integer `x` is a multiple of `k` if there exists an integer `n` such that `x =
    n * k`. `0` is **always** a multiple of `k`.

    """

    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the remainder when sum up to the current index is divided by k
        # Initialized with {0: -1} to handle the case where the sum of a subarray from the beginning is a multiple of k
        remainder_dict = {0: -1}
        current_sum = 0

        # Iterate through the array
        for i, num in enumerate(nums):
            # Add the current number to the running sum
            current_sum += num

            # Compute the remainder of the running sum divided by k
            if k != 0:
                remainder = current_sum % k
            else:
                remainder = current_sum

            # If this remainder has been seen before
            if remainder in remainder_dict:
                # Check the length of the subarray
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                # Otherwise, store the index of this remainder
                remainder_dict[remainder] = i

        # If no valid subarray is found, return False
        return False

    checkSubarraySum = check_subarray_sum
