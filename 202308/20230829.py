# https://leetcode.com/problems/minimum-penalty-for-a-shop/
import heapq


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """2483. Minimum Penalty for a Shop

        You are given the customer visit log of a shop represented by a 0-indexed string
        `customers` consisting only of characters `'N'` and `'Y'`:
        - if the `ith` character is `'Y'`, it means that customers come at the `ith` hour
        - whereas `'N'` indicates that no customers come at the `ith` hour.

        If the shop closes at the `jth` hour `(0 <= j <= n)`, the penalty is calculated as follows:
        - For every hour when the shop is open and no customers come, the penalty increases by 1.
        - For every hour when the shop is closed and customers come, the penalty increases by 1.

        Return _the **earliest** hour at which the shop must be closed to incur a **minimum** penalty._

        Note that if a shop closes at the `jth` hour, it means the shop is closed at the hour `j`.

        Args:
            customers (str): A sequence of characters `"Y|N"` that represent customers arriving
                at the shop at the hour it's index maps to

        Returns:
            int: the **earliest** hour at which the shop must be closed to incur a **minimum** penalty
        """
        n = len(customers)
        # create a holding array for values of tuples
        prefix_sum = [0] * (n + 1)

        # Calculate prefix sum of penalties
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (customers[i] == "N")

        min_heap = []
        for closing_hour in range(n + 1):
            penalty = prefix_sum[closing_hour] + (
                n - closing_hour - (prefix_sum[n] - prefix_sum[closing_hour])
            )
            heapq.heappush(min_heap, (penalty, closing_hour))

        return heapq.heappop(min_heap)[1]
