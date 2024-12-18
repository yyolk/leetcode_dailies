# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


class Solution:
    """1475. Final Prices With a Special Discount in a Shop

    You are given an integer array `prices` where `prices[i]` is the price of the `ith`
    item in a shop.

    There is a special discount for items in the shop. If you buy the `ith` item, then
    you will receive a discount equivalent to `prices[j]` where `j` is the minimum index
    such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any
    discount at all.

    Return an integer array `answer` where `answer[i]` is the final price you will pay
    for the `ith` item of the shop, considering the special discount."""

    def final_prices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        # Start with a copy of the original prices
        answer = prices.copy()

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    # We've found the first applicable discount, no need to look further
                    break

        return answer

    finalPrices = final_prices
