# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range


class Solution:
    """1523. Count Odd Numbers in an Interval Range

    Given two non-negative integers low and high. Return the
    count of odd numbers between low and high (inclusive).
    """
    def count_odds(self, low: int, high: int) -> int:
        # Count of odds from 0 to high inclusive: (high + 1) // 2
        # Count of odds from 0 to low-1 inclusive: low // 2
        # Subtract to get count in [low, high]
        return (high + 1) // 2 - (low // 2)

    countOdds = count_odds