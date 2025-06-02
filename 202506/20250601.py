# https://leetcode.com/problems/distribute-candies-among-children-ii/


class Solution:
    """2929. Distribute Candies Among Children II

    You are given two positive integers `n` and `limit`.

    Return *the **total number** of ways to distribute* `n` *candies among* `3`
    *children such that no child gets more than* `limit` *candies.*"""

    def distribute_candies(self, n: int, limit: int) -> int:
        def comb2(m):
            """Helper function to compute C(m, 2) = m*(m-1)/2 if m >= 2, else 0."""
            return m * (m - 1) // 2 if m >= 2 else 0

        # Use inclusion-exclusion to find the number of valid distributions
        return (
            comb2(n + 2)
            - 3 * comb2(n - limit + 1)
            + 3 * comb2(n - 2 * limit)
            - comb2(n - 3 * limit - 1)
        )

    distributeCandies = distribute_candies
