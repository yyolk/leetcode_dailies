# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock


class Solution:
    """2110. Number of Smooth Descent Periods of a Stock

    You are given an integer array prices representing the daily price
    history of a stock, where prices[i] is the stock price on the ith day.

    A smooth descent period consists of one or more contiguous days such
    that the price on each day is lower than the price on the preceding
    day by exactly 1. The first day of the period is exempted from this
    rule.

    Return the number of smooth descent periods.
    """
    def get_descent_periods(self, prices: list[int]) -> int:
        n = len(prices)
        ans = 0
        streak = 0
        for i in range(n):
            # Reset streak if descent breaks or at start
            if i == 0 or prices[i] != prices[i - 1] - 1:
                streak = 1
            # Otherwise extend current descent streak
            else:
                streak += 1
            # All subarrays ending at i form streak many periods
            ans += streak
        return ans

    getDescentPeriods = get_descent_periods