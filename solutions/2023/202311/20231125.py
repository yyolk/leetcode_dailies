# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/


class Solution:
    """1685. Sum of Absolute Differences in a Sorted Array

    You are given an integer array `nums` sorted in **non-decreasing** order.

    Build and return *an integer array* `result` *with the same length as* `nums` *such
    that* `result[i]` *is equal to the **summation of absolute differences** between*
    `nums[i]` *and all the other elements in the array.*

    In other words, `result[i]` is equal to `sum(|nums[i]-nums[j]|)` where `0 <= j <
    nums.length` and `j != i` (**0-indexed**).
    """

    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        """Builds and returns an integer array result with the same length as nums...

        Builds and returns an integer array result with the same length as nums,
        where result[i] is equal to the summation of absolute differences between
        nums[i] and all the other elements in the array.

        Args:
            nums: A sorted integer array.

        Returns:
            An integer array with the same length as nums.
        """
        n = len(nums)
        result = []

        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialize prefix_sum
        prefix_sum = 0

        # Calculate the result array on the fly
        for i in range(n):
            # Calculate the right side sum and difference
            right_sum = (total_sum - prefix_sum) - (n - i) * nums[i]

            # Calculate the left side sum and difference
            left_sum = i * nums[i] - prefix_sum

            # Append the result for the current element
            result.append(left_sum + right_sum)

            # Update prefix_sum for the next iteration
            prefix_sum += nums[i]

        return result

    getSumAbsoluteDifferences = get_sum_absolute_differences
