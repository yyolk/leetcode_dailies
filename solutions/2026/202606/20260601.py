# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/


class Solution:
    """2144. Minimum Cost of Buying Candies With Discount

    A shop is selling candies at a discount. For every two candies sold, the shop
    gives a third candy for free. The customer can choose any candy to take away for
    free as long as the cost of the chosen candy is less than or equal to the minimum
    cost of the two candies bought.

    For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer
    buys candies with costs 2 and 3, they can take the candy with cost 1 for free,
    but not the candy with cost 4.

    Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith
    candy, return the minimum cost of buying all the candies.
    """

    def minimum_cost(self, cost: list[int]) -> int:
        # Sort costs descending: ensures every 3rd candy qualifies as free
        # (it is <= min of the two higher-cost candies paid immediately before)
        cost.sort(reverse=True)
        # Pay for all except free candies at indices 2, 5, 8, ... (0-based)
        return sum(cost) - sum(cost[2::3])

    minimumCost = minimum_cost
