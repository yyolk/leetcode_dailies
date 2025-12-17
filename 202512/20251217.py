# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v


class Solution:
    """3573. Best Time to Buy and Sell Stock V

    You are given an integer array prices where prices[i] is the price of a stock
    in dollars on the ith day, and an integer k.

    You are allowed to make at most k transactions, where each transaction can
    be either of the following:

    Normal transaction: Buy on day i, then sell on a later day j where i < j.
    You profit prices[j] - prices[i].

    Short selling transaction: Sell on day i, then buy back on a later day j
    where i < j. You profit prices[i] - prices[j].

    Note that you must complete each transaction before starting another.
    Additionally, you can't buy or sell on the same day you are selling or
    buying back as part of a previous transaction.

    Return the maximum total profit you can earn by making at most k
    transactions.
    """
    def maximum_profit(self, prices: list[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # Large negative sentinel for impossible states
        NEG = -10**18

        # max_pos[t]: max over possible opens (prev_profit_with_t + open_price)
        # max_neg[t]: max over possible opens (prev_profit_with_t - open_price)
        max_pos = [NEG] * (k + 1)
        max_neg = [NEG] * (k + 1)

        # prev_dp[j]: max profit with exactly j completed transactions up to previous day
        prev_dp = [0] + [NEG] * k

        for i in range(1, n + 1):
            p = prices[i - 1]

            # Carry over skip (no action on current day)
            curr_dp = prev_dp[:]

            for j in range(1, k + 1):
                # Compute max prev_profit + |p - open_price| in O(1)
                add1 = NEG if max_neg[j - 1] == NEG else p + max_neg[j - 1]
                add2 = NEG if max_pos[j - 1] == NEG else -p + max_pos[j - 1]
                close_profit = max(add1, add2)

                # Update if closing a transaction on current day
                if close_profit != NEG:
                    curr_dp[j] = max(curr_dp[j], close_profit)

            # Add current day as a possible open point (using state before any action today)
            for t in range(k + 1):
                if prev_dp[t] != NEG:
                    max_pos[t] = max(max_pos[t], prev_dp[t] + p)
                    max_neg[t] = max(max_neg[t], prev_dp[t] - p)

            prev_dp = curr_dp

        # Maximum over all possible number of transactions (<= k)
        ans = 0
        for val in prev_dp:
            if val != NEG:
                ans = max(ans, val)
        return ans

    maximumProfit = maximum_profit