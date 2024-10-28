# https://leetcode.com/problems/longest-square-streak-in-an-array/


class Solution:
    """2501. Longest Square Streak in an Array

    You are given an integer array `nums`. A subsequence of `nums` is called a **square
    streak** if:

    * The length of the subsequence is at least `2`, and

    * **after** sorting the subsequence, each element (except the first element) is the
    **square** of the previous number.

    Return *the length of the **longest square streak** in* `nums`*, or return* `-1` *if
    there is no **square streak**.*

    A **subsequence** is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.

    """

    def longest_square_streak(self, nums: list[int]) -> int:
        # Sort the array to facilitate finding squares
        nums.sort()
        # Use a dictionary to keep track of the longest streak ending with each number
        dp = {num: 1 for num in nums}
        max_streak = -1
        
        for i in range(1, len(nums)):
            sqrt = int(nums[i]**0.5)
            if sqrt * sqrt == nums[i] and sqrt in dp:
                # If the current number is a perfect square of a previous number,
                # extend the streak
                dp[nums[i]] = dp[sqrt] + 1
                max_streak = max(max_streak, dp[nums[i]])
        
        # If max_streak is still 1, no valid square streak was found
        return max_streak if max_streak > 1 else -1

    longestSquareStreak = longest_square_streak
