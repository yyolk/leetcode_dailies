# https://leetcode.com/problems/maximum-ice-cream-bars/


class Solution:
    """1833. Maximum Ice Cream Bars

    It is a sweltering summer day, and a boy wants to buy some ice cream bars.
    At the store, there are n ice cream bars. You are given an array costs of
    length n, where costs[i] is the price of the ith ice cream bar in coins.
    The boy initially has coins coins to spend, and he wants to buy as many ice
    cream bars as possible.

    Note: The boy can buy the ice cream bars in any order.

    Return the maximum number of ice cream bars the boy can buy with coins coins.
    You must solve the problem by counting sort.
    """

    def max_ice_cream(self, costs: list[int], coins: int) -> int:
        # Count freq of each possible cost (1 <= costs[i] <= 10^5)
        MAX = 100000
        count = [0] * (MAX + 1)
        for cost in costs:
            count[cost] += 1
        bars = 0
        # Buy cheapest possible using counting sort iteration
        for price in range(1, MAX + 1):
            if coins < price:
                # Cannot afford this or any higher price
                break
            can_buy = min(count[price], coins // price)
            bars += can_buy
            coins -= can_buy * price
        return bars

    maxIceCream = max_ice_cream
