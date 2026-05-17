# https://leetcode.com/problems/buy-two-chocolates/


class Solution:
    """2706. Buy Two Chocolates

    You are given an integer array `prices` representing the prices of various
    chocolates in a store. You are also given a single integer `money`, which represents
    your initial amount of money.

    You must buy **exactly** two chocolates in such a way that you still have some
    **non-negative** leftover money. You would like to minimize the sum of the prices of
    the two chocolates you buy.

    Return *the amount of money you will have leftover after buying the two chocolates*.
    If there is no way for you to buy two chocolates without ending up in debt, return
    `money`. Note that the leftover must be non-negative.
    """

    def buy_choco(self, prices: list[int], money: int) -> int:
        """Buy Chocolates.

        Args:
            prices: The input prices of chocolates available to buy.
            money: The starting money to buy chocolate.

        Returns:
            The leftover money subtracted by any that was spent.
        """
        # Initialize length of prices.
        n = len(prices)

        # Initialize the minimum leftover money to the maximum possible value.
        min_leftover = float("inf")

        # Iterate over every pair of chocolates.
        for first in range(n):
            for second in range(first + 1, n):
                # Sum the two chocolate prices.
                cost = prices[first] + prices[second]

                # If the sum of prices is less than the min leftover.
                if cost < min_leftover:
                    # Update min leftover.
                    min_leftover = cost

        # We can buy chocolates if we have enough money.
        if min_leftover <= money:
            # The amount we have left.
            return money - min_leftover

        # We cannot buy chocolates.
        return money

    buyChoco = buy_choco
