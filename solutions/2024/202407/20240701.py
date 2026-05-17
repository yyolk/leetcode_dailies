# https://leetcode.com/problems/three-consecutive-odds/


class Solution:
    """1550. Three Consecutive Odds

    Given an integer array `arr`, return `true` if there are three consecutive odd
    numbers in the array. Otherwise, return `false`.

    """

    def three_consecutive_odds(self, arr: list[int]) -> bool:
        # Iterate through the array
        for i in range(len(arr) - 2):
            # Check if the current number and the next two numbers are odd
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False

    threeConsecutiveOdds = three_consecutive_odds
