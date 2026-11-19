# https://leetcode.com/problems/minimum-score-by-changing-two-elements/


class Solution:
    """2567. Minimum Score by Changing Two Elements

    You are given an integer array `nums`.

    * The **low** score of `nums` is the **minimum** absolute difference
      between any two integers.

    * The **high** score of `nums` is the **maximum** absolute difference
      between any two integers.

    * The **score** of `nums` is the sum of the **high** and **low** scores.

    Return the **minimum score** after **changing two elements** of `nums`.

    Constraints:

    * `3 <= nums.length <= 105`

    * `1 <= nums[i] <= 109`
    """

    def minimize_sum(self, nums: list[int]) -> int:
        """Return min score after changing two elements.

        Sort then take the min range that covers all but two elements,
        since the low score can always be made zero.

        Args:
            nums (list[int]): The input array.

        Returns:
            int: The minimum possible score.
        """
        # Sort to identify the extremes easily.
        nums.sort()
        n = len(nums)
        # Low score can always be 0 by equating two changed values.
        # Minimize high score = smallest range covering n-2 elements.
        # Drop two smallest, two largest, or one of each.
        return min(
            nums[n - 1] - nums[2],
            nums[n - 2] - nums[1],
            nums[n - 3] - nums[0],
        )

    minimizeSum = minimize_sum
