# https://leetcode.com/problems/rearranging-fruits/
from collections import Counter


class Solution:
    """2561. Rearranging Fruits

    You have two fruit baskets containing `n` fruits each. You are given two
    **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit
    in each basket. You want to make both baskets **equal**. To do so, you can use the
    following operation as many times as you want:

    * Chose two indices `i` and `j`, and swap the `ith`fruit of `basket1` with the `jth`
    fruit of `basket2`.

    * The cost of the swap is `min(basket1[i],basket2[j])`.

    Two baskets are considered equal if sorting them according to the fruit cost makes
    them exactly the same baskets.

    Return *the minimum cost to make both the baskets equal or* `-1` *if impossible.*"""

    def min_cost(self, basket1: list[int], basket2: list[int]) -> int:
        # Create a Counter for basket1 to count fruit frequencies
        count = Counter(basket1)
        # Subtract the Counter of basket2 to find differences in frequencies
        count.subtract(Counter(basket2))
        # Initialize an empty list to hold fruits that need to be swapped
        swapped = []
        # Iterate over each fruit and its net frequency difference
        for num, freq in count.items():
            # If the frequency difference is odd, it's impossible to equalize
            if freq % 2 != 0:
                return -1
            # Add the fruit to swapped list abs(freq)//2 times (half the swaps needed)
            swapped += [num] * (abs(freq) // 2)
        # If no swaps are needed, return 0 cost
        if not swapped:
            return 0
        # Find the smallest fruit cost in either basket for potential swap costs
        min_num = min(min(basket1), min(basket2))
        # Sort the swapped list to prioritize smaller costs
        swapped.sort()
        # Calculate half the length of swapped, as we process in pairs effectively
        k = len(swapped) // 2
        # Initialize cost to 0
        cost = 0
        # Loop over the first k elements in sorted swapped
        for i in range(k):
            # Add the minimum between the fruit cost or twice the smallest fruit cost
            cost += min(swapped[i], 2 * min_num)
        # Return the total computed cost
        return cost
    minCost = min_cost
