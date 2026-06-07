# https://leetcode.com/problems/candy/


class Solution:
    """135. Candy

    There are `n` children standing in a line. Each child is assigned a rating value given
    in the integer array `ratings`.

    You are giving candies to these children subjected to the following requirements:

    * Each child must have at least one candy.

    * Children with a higher rating get more candies than their neighbors.

    Return *the minimum number of candies you need to have to distribute the candies to the
    children*.
    """

    def candy(self, ratings: list[int]) -> int:
        """Calculates the minimum number of candies needed to distribute to the children.

        Proposed solution.

        Args:
            ratings (list of int): a list of integer ratings that map to a single child

        Returns:
            int: the number of candies needed to distribute to the children
        """
        # Init the number of candies to distribute, starting with the len(ratings)
        num_candies = len(ratings)
        # Init the number of candies for each child
        child_candies = [1] * num_candies

        # Distribute candies based on rating
        # Traverse from left to right
        for i in range(1, num_candies):
            if ratings[i] > ratings[i - 1]:
                child_candies[i] = child_candies[i - 1] + 1
        # Traverse from right to left
        for i in range(num_candies - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and child_candies[i] <= child_candies[i + 1]:
                child_candies[i] = child_candies[i + 1] + 1

        # Return the minimum number of candies needed to distribute to the children
        return sum(child_candies)
