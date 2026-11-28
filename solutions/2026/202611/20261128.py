# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/


class Solution:
    """3947. Maximum Number of Items From Sale II

    You are given a 2D integer array items, where items[i] = [factor_i, price_i]
    represents the ith item. You are also given an integer budget.

    There are unlimited copies of each item available for purchase. You may buy
    any number of copies of any items such that the total cost of the purchased
    copies is at most budget.

    After buying items, you may receive free copies according to the following
    rules:

    * Each purchased copy of item i can give you at most one free copy of
      another item j.

    * The free item must satisfy i != j and factor_i divides factor_j.

    * For each ordered pair (i, j), you can receive a free copy of item j from
      purchases of item i at most once, regardless of how many copies of item i
      you buy.

    * The same item j can be received multiple times for free if it is received
      from purchases of different item types.

    Return the maximum total number of item copies you can obtain, including
    both purchased copies and free copies, while spending at most budget on
    purchased items.

    Constraints:

    * 1 <= items.length <= 10**5

    * items[i] = [factor_i, price_i]

    * 1 <= factor_i <= items.length

    * 1 <= price_i <= 10**9

    * 1 <= budget <= 10**9
    """

    def maximum_sale_items(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        # Count frequency of each factor (factors are in 1..n).
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1

        # multiples[f] = number of items whose factor is a multiple of f.
        # Computed in O(n log n) by iterating multiples.
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            for k in range(f, n + 1, f):
                multiples[f] += freq[k]

        min_price = min(price for _, price in items)
        # Collect (price, gain) for items that can provide free copies.
        # gain[i] = number of other items j where factor_i divides factor_j.
        doubles = []
        for factor, price in items:
            gain = multiples[factor] - 1
            if gain > 0:
                doubles.append((price, gain))

        # Sort by price so we consider cheapest double opportunities first.
        doubles.sort()

        total = 0
        remaining = budget
        # Only take a double-value purchase (cost p for +2 items) when it is
        # strictly better than spending the same money on the cheapest singles
        # (cost min_price for +1). Equality can be suboptimal due to remainders.
        threshold = 2 * min_price
        for price, gain in doubles:
            if price >= threshold:
                break
            can_take = remaining // price
            take = min(gain, can_take)
            if take == 0:
                break
            total += take * 2
            remaining -= take * price
            if take < gain:
                break

        # Spend any leftover budget on the cheapest item (value-1 purchases).
        total += remaining // min_price
        return total

    maximumSaleItems = maximum_sale_items
