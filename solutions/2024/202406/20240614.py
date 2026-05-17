# https://leetcode.com/problems/minimum-increment-to-make-array-unique/


class Solution:
    """945. Minimum Increment to Make Array Unique

    You are given an integer array `nums`. In one move, you can pick an index `i` where
    `0 <= i < nums.length` and increment `nums[i]` by `1`.

    Return *the minimum number of moves to make every value in* `nums` ***unique***.

    The test cases are generated so that the answer fits in a 32-bit integer.

    """

    def min_increment_for_unique(self, nums: list[int]) -> int:
        # Sort the array to handle duplicates easily
        nums.sort()

        # Initialize the move count to 0
        moves = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current number is less than or equal to the previous number
            if nums[i] <= nums[i - 1]:
                # Calculate the increment needed to make it unique
                increment = nums[i - 1] - nums[i] + 1
                # Add the increment to the current number
                nums[i] += increment
                # Add the increment to the total move count
                moves += increment

        return moves

    minIncrementForUnique = min_increment_for_unique
