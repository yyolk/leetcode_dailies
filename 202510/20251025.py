# https://leetcode.com/problems/calculate-money-in-leetcode-bank/


class Solution:
    """1716. Calculate Money in Leetcode Bank

    Hercy wants to save money for his first car. He puts money in the Leetcode bank
    **every day**.

    He starts by putting in `$1` on Monday, the first day. Every day from Tuesday to
    Sunday, he will put in `$1` more than the day before. On every subsequent Monday, he
    will put in `$1` more than the **previous Monday**.

    Given `n`, return *the total amount of money he will have in the Leetcode bank at
    the end of the* `nth` *day.*"""

    def total_money(self, n: int) -> int:
        # Calculate number of complete weeks
        w = n // 7
        # Calculate remaining days after complete weeks
        r = n % 7
        # Sum for complete weeks: (7w^2 + 49w) / 2
        complete_sum = (7 * w * w + 49 * w) // 2
        # Monday deposit for the next week
        m = w + 1
        # Sum for remaining days: r * m + r*(r-1)/2
        remaining_sum = r * m + (r * (r - 1)) // 2
        # Total money is sum of complete weeks and remaining days
        return complete_sum + remaining_sum

    totalMoney = total_money
