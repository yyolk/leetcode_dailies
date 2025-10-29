# https://leetcode.com/problems/make-array-elements-equal-to-zero/


class Solution:
    """3354. Make Array Elements Equal to Zero

    You are given an integer array `nums`.

    Start by selecting a starting position `curr` such that `nums[curr] == 0`, and
    choose a movement **direction** of either left or right.

    After that, you repeat the following process:

    * If `curr` is out of the range `[0, n - 1]`, this process ends.

    * If `nums[curr] == 0`, move in the current direction by **incrementing** `curr` if
    you are moving right, or **decrementing** `curr` if you are moving left.

    * Else if `nums[curr] > 0`:

      + Decrement `nums[curr]` by 1.

      + **Reverse** your movement direction (left becomes right and vice versa).

      + Take a step in your new direction.

    A selection of the initial position `curr` and movement direction is considered
    **valid** if every element in `nums` becomes 0 by the end of the process.

    Return the number of possible **valid** selections."""

    def count_valid_selections(self, nums: list[int]) -> int:
        # Compute the total sum of all elements in the array
        total_sum = sum(nums)

        # Initialize the count of valid selections and the left sum
        valid_count = 0
        left_sum = 0

        # Iterate through each element in the array
        for num in nums:
            if num != 0:
                # Add the non-zero element to the left sum, as it is now to the left of future positions
                left_sum += num
            else:
                # At a potential starting zero position, calculate the right sum implicitly
                # Check if left sum equals right sum (balanced)
                if left_sum * 2 == total_sum:
                    # Both directions are valid when sums are equal
                    valid_count += 2
                # Check if the absolute difference between left and right sums is exactly 1
                elif abs(left_sum * 2 - total_sum) == 1:
                    # One direction is valid when sums differ by 1
                    valid_count += 1

        return valid_count

    countValidSelections = count_valid_selections
