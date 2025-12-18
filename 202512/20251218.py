# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy

from itertools import accumulate

class Solution:
    """3652. Best Time to Buy and Sell Stock using Strategy

    Given prices and strategy arrays of equal length n, and even k.
    Profit = sum(strategy[i] * prices[i] for all i).
    Optionally modify one segment of k consecutive days:
    set first k//2 days to hold (0), last k//2 days to sell (1).
    Return the maximum achievable profit.
    Constraints: 2 <= n <= 1e5, k even, 2 <= k <= n.
    """
    def max_profit(self, prices: list[int], strategy: list[int], k: int) -> int:
        n = len(prices)
        half_k = k // 2
        
        # prefix[0] = 0, prefix[i+1] = sum of strategy[0..i] * prices[0..i]
        prefix_profit = list(accumulate(
            (strategy[i] * prices[i] for i in range(n)), initial=0))
        
        total_profit = prefix_profit[n]  # original profit without modification
        
        max_profit = total_profit  # at least the original
        
        if n < k:
            return max_profit
        
        # Initial window: start=0, modified sell contribution = sum(prices[half_k : k])
        current_sell_sum = sum(prices[half_k : k])
        
        # Profit with modification on [0, k): total - contrib[0:k) + new_contrib
        window_gain = current_sell_sum - (prefix_profit[k] - prefix_profit[0])
        max_profit = max(max_profit, total_profit + window_gain)
        
        # Slide the window from start=1 to n-k
        for start in range(1, n - k + 1):
            # Update sliding sell sum: add new sell day, remove old hold day
            current_sell_sum += prices[start + k - 1] - prices[start + half_k - 1]
            
            # New window gain
            window_gain = current_sell_sum - (prefix_profit[start + k] - prefix_profit[start])
            
            max_profit = max(max_profit, total_profit + window_gain)
        
        return max_profit

    maxProfit = max_profit