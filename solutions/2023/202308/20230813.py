# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
from functools import cache


class Solution:
    """2443. Check if There is a Valid Partition For The Array

    You are given a **0-indexed** integer array `nums`. You have to partition the array
    into one or more **contiguous** subarrays.

    We call a partition of the array **valid** if each of the obtained subarrays
    satisfies **one** of the following conditions:

    1. The subarray consists of **exactly** `2,` equal elements. For example, the
    subarray `[2,2]` is good.

    2. The subarray consists of **exactly** `3,` equal elements. For example, the
    subarray `[4,4,4]` is good.

    3. The subarray consists of **exactly** `3` consecutive increasing elements, that
    is, the difference between adjacent elements is `1`. For example, the subarray
    `[3,4,5]` is good, but the subarray `[1,3,5]` is not.

    Return `true` *if the array has **at least** one valid partition*. Otherwise, return
    `false`.
    """

    def valid_partition(self, nums: list[int]) -> bool:
        """Determine if input has a valid partition.

        Args:
            nums: Input 0-indexed integer array to partition into one or more
                contiguous subarrays.

        Returns:
            True if the array has at least one valid partition, False otherwise.
        """
        n = len(nums)

        @cache
        def is_valid_partition(index: int) -> bool:
            """Inner function to solve for valid partition with recursion."""
            # Base case: if the index reaches the end of the array, return True.
            if index == n:
                return True

            # Iterate over possible sizes of subarrays (2 or 3).
            for size in (2, 3):
                # Check if the current subarray size is within bounds.
                if index + size <= n:
                    # Check conditions for each subarray size.
                    if size == 2 and nums[index] == nums[index + 1]:
                        # Recursively check the next subarray.
                        if is_valid_partition(index + size):
                            return True
                    elif (
                        size == 3 and nums[index] == nums[index + 1] == nums[index + 2]
                    ):
                        if is_valid_partition(index + size):
                            return True
                    elif (
                        size == 3
                        and nums[index] == nums[index + 1] - 1
                        and nums[index + 1] == nums[index + 2] - 1
                    ):
                        if is_valid_partition(index + size):
                            return True

            # If none of the conditions are satisfied, return False.
            return False

        # Start checking partitions from the beginning of the array.
        return is_valid_partition(0)

    validPartition = valid_partition
