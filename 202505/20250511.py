# https://leetcode.com/problems/three-consecutive-odds/


class Solution:
    """1550. Three Consecutive Odds

    Given an integer array `arr`, return `true` if there are three consecutive odd
    numbers in the array. Otherwise, return `false`."""

    def three_consecutive_odds(self, arr: list[int]) -> bool:
        # Check every triplet using zip
        for a, b, c in zip(arr, arr[1:], arr[2:]):
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                return True
        return False
    threeConsecutiveOdds = three_consecutive_odds
