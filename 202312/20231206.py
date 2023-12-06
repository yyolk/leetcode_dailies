# https://leetcode.com/problems/calculate-money-in-leetcode-bank/


class Solution:
    """1716. Calculate Money in Leetcode Bank

    Hercy wants to save money for his first car. He puts money in the Leetcode bank
    **every day**.

    He starts by putting in `$1` on Monday, the first day. Every day from Tuesday to
    Sunday, he will put in `$1` more than the day before. On every subsequent Monday, he
    will put in `$1` more than the **previous Monday**.

    Given `n`, return *the total amount of money he will have in the Leetcode bank at
    the end of the* `nth` *day.*
    """

    def total_money(self, n: int) -> int:
        """Calculate the money in the bank on the nth day.

        Args:
            n: The day to calculate what the total amount of money will be.

        Returns:
            The total amount of money in the Leetcode bank at the end of the nth day.
        """
        ans = 0
        monday = 1

        while n > 0:
            for day in range(min(n, 7)):
                ans += monday + day

            n -= 7
            monday += 1

        return ans

    totalMoney = total_money
