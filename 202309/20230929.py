# https://leetcode.com/problems/monotonic-array/


class Solution:
    """896. Monotonic Array

    An array is **monotonic** if it is either monotone increasing or monotone decreasing.

    An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An
    array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

    Given an integer array `nums`, return `true` *if the given array is monotonic, or*
    `false` *otherwise*.
    """

    def isMonotonic(self, nums: list[int]) -> bool:
        """Checks if an input array of nums is monotonic.

        Proposed solution that checks each item until the direction changes.

        Args:
            nums (list of int): input nums to check for monotonic quality

        Returns:
            bool: input is monotonic increasing or monotonic decreasing
        """
        # This will always be True
        if len(nums) == 1:
            return True

        # Direction starts off undetermined
        direction = 0

        # Iterate over all numbers in input nums
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i] < nums[i - 1]:
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False

        # We passed the monotomic test, it's True
        return True
