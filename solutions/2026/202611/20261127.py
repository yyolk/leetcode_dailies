# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/


class Solution:
    """3946. Maximum Number of Items From Sale I

    You are given a 2D integer array items, where items[i] = [factor_i, price_i]
    represents the ith item. You are also given an integer budget.

    There are unlimited copies of each item available for purchase. You may buy
    any number of copies of any items such that the total cost of the purchased
    copies is at most budget.

    After buying items, you may receive free copies according to the following
    rules:

    * For each item i that you bought at least one copy of, you receive one free
      copy of every item j such that j != i and factor_i divides factor_j.

    * Buying multiple copies of the same item i does not give additional free
      copies through item i.

    * The same item j can be received multiple times for free if it is received
      from purchases of different item types.

    Return the maximum total number of item copies you can obtain, including
    both purchased copies and free copies, while spending at most budget on
    purchased items.

    Constraints:

    * 1 <= items.length <= 1000
    * items[i] = [factor_i, price_i]
    * 1 <= factor_i, price_i <= 1500
    * 1 <= budget <= 1500
    """

    def maximum_sale_items(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        if n == 0:
            return 0

        # Count free items granted by the first purchase of each item type.
        free_counts = [0] * n
        for i in range(n):
            factor_i = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    free_counts[i] += 1

        # First purchase of item i yields 1 purchased + free_counts[i] free copies.
        first_values = [1 + free_counts[i] for i in range(n)]
        prices = [items[i][1] for i in range(n)]
        min_price = min(prices)

        # 0-1 knapsack over the at-most-once first purchases.
        # dp[c] = max items from first purchases spending exactly c.
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            cost = prices[i]
            val = first_values[i]
            if cost > budget:
                continue
            # Backwards scan enforces taking each item at most once.
            for c in range(budget - cost, -1, -1):
                if dp[c] >= 0:
                    new_c = c + cost
                    dp[new_c] = max(dp[new_c], dp[c] + val)

        # Spend any leftover budget on the cheapest item (each yields 1 copy).
        max_items = 0
        for spent in range(budget + 1):
            if dp[spent] >= 0:
                extras = (budget - spent) // min_price
                max_items = max(max_items, dp[spent] + extras)

        return max_items

    maximumSaleItems = maximum_sale_items
