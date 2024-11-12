# https://leetcode.com/problems/most-beautiful-item-for-each-query/
from itertools import accumulate
from bisect import bisect_right


class Solution:
    """2070. Most Beautiful Item for Each Query

    You are given a 2D integer array `items` where `items[i] = [pricei, beautyi]`
    denotes the **price** and **beauty** of an item respectively.

    You are also given a **0\\-indexed** integer array `queries`. For each `queries[j]`,
    you want to determine the **maximum beauty** of an item whose **price** is **less
    than or equal** to `queries[j]`. If no such item exists, then the answer to this
    query is `0`.

    Return *an array* `answer` *of the same length as* `queries` *where* `answer[j]` *is
    the answer to the* `jth` *query*.

    """

    def maximum_beauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        # Unzip and sort items by price, then zip back together into price and beauty lists
        price, beauty = zip(*sorted(items))

        # Use accumulate to compute the maximum beauty seen so far for each price point
        # This creates a list where each element is the max beauty for that price or lower
        beauty = list(accumulate(beauty, lambda x, y: max(x, y)))

        # For each query:
        # - If the query price is less than the smallest item price, return 0
        # - Otherwise, find the position to insert the query price in the sorted price list 
        #   and take the beauty at the previous index (since we want <= query)
        return [
            # If query price is less than the cheapest item, no item matches, so return 0
            0 if q < price[0] else 
            # Use binary search to find where q would go in price list, 
            # then take the beauty of the item just before this position
            beauty[bisect_right(price, q) - 1] for q in queries
        ]

    maximumBeauty = maximum_beauty
