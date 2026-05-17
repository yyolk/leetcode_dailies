# https://leetcode.com/problems/candy/


class Solution:
    """135. Candy

    There are `n` children standing in a line. Each child is assigned a rating value
    given in the integer array `ratings`.

    You are giving candies to these children subjected to the following requirements:

    * Each child must have at least one candy.

    * Children with a higher rating get more candies than their neighbors.

    Return *the minimum number of candies you need to have to distribute the candies to
    the children*."""

    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        # Handle edge case: empty array (though constraints guarantee n >= 1)
        if n == 0:
            return 0

        # Initialize candies array with 1 candy per child
        candies = [1] * n

        # Left to right pass: ensure higher ratings get more candies than left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass: ensure higher ratings get more candies than right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the total number of candies
        return sum(candies)
