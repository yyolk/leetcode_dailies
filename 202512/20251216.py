# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts


class Solution:
    """3562. Maximum Profit from Trading Stocks with Discounts

    Given n employees (1 to n, 1 is CEO), present/future prices (0-indexed lists
    for employees 1 to n), hierarchy as [boss, subordinate] pairs forming a tree,
    and budget.

    If a boss buys their own stock, direct subordinates buy at floor(price/2).
    Maximize total profit (sum of (future - effective_cost) for bought stocks)
    with total effective_cost <= budget. Each stock buyable at most once.
    """

    def max_profit(self, n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
        # Build adjacency list (0-based indexing, root 0 for employee 1)
        tree = [[] for _ in range(n)]
        for boss, sub in hierarchy:
            tree[boss - 1].append(sub - 1)

        import functools
        import math

        @functools.lru_cache(None)
        def dfs(u: int) -> tuple[list[int], list[int]]:
            # Combined dp from children when not buying u (children no discount)
            no_disc_children = [0] * (budget + 1)
            # Combined dp from children when buying u (children get discount)
            with_disc_children = [0] * (budget + 1)

            for v in tree[u]:
                child_no, child_with = dfs(v)
                # Merge child contributions
                no_disc_children = merge(no_disc_children, child_no)
                with_disc_children = merge(with_disc_children, child_with)

            # dp_no: subtree max profits when u has no incoming discount
            dp_no = no_disc_children[:]
            # dp_with: subtree max profits when u has incoming discount
            dp_with = no_disc_children[:]

            # Option: buy u at full price (only possible/used when no incoming discount)
            full_cost = present[u]
            full_profit = future[u] - full_cost
            for b in range(full_cost, budget + 1):
                dp_no[b] = max(dp_no[b], with_disc_children[b - full_cost] + full_profit)

            # Option: buy u at half price (only when incoming discount)
            half_cost = present[u] // 2
            half_profit = future[u] - half_cost
            for b in range(half_cost, budget + 1):
                dp_with[b] = max(dp_with[b], with_disc_children[b - half_cost] + half_profit)

            return dp_no, dp_with

        def merge(a: list[int], b: list[int]) -> list[int]:
            # Convolution: max profit over all cost splits
            res = [-math.inf] * (budget + 1)
            for i in range(budget + 1):
                if a[i] == -math.inf:
                    continue
                for j in range(budget + 1 - i):
                    res[i + j] = max(res[i + j], a[i] + b[j])
            return res

        # Root has no incoming discount; take max over all costs <= budget
        return max(dfs(0)[0])

    maxProfit = max_profit