# https://leetcode.com/problems/soup-servings/


class Solution:
    """808. Soup Servings

    You have two soups, **A** and **B**, each starting with `n` mL. On every turn, one
    of the following four serving operations is chosen *at random*, each with
    probability `0.25` **independent** of all previous turns:

    * pour 100 mL from type A and 0 mL from type B

    * pour 75 mL from type A and 25 mL from type B

    * pour 50 mL from type A and 50 mL from type B

    * pour 25 mL from type A and 75 mL from type B

    **Note:**

    * There is no operation that pours 0 mL from A and 100 mL from B.

    * The amounts from A and B are poured *simultaneously* during the turn.

    * If an operation asks you to pour **more than** you have left of a soup, pour all
    that remains of that soup.

    The process stops immediately after any turn in which *one of the soups* is used up.

    Return the probability that A is used up *before* B, plus half the probability that
    both soups are used up in the **same turn**. Answers within `10-5` of the actual
    answer will be accepted."""

    def soup_servings(self, n: int) -> float:
        # Handle the edge case where n is 0, both soups are already empty
        if n == 0:
            return 0.5
        # Scale down the problem by dividing by 25, using ceiling division
        m = (n + 24) // 25
        # For large m, the probability is very close to 1, within the tolerance
        if m >= 179:
            return 1.0
        # Define the operations in units of 25 mL
        ops = [(4, 0), (3, 1), (2, 2), (1, 3)]
        # Use memoization for the recursive function
        from functools import cache

        @cache
        def dp(a: int, b: int) -> float:
            # Base case: both soups empty
            if a <= 0 and b <= 0:
                return 0.5
            # Base case: A empty, B not
            if a <= 0:
                return 1.0
            # Base case: B empty, A not
            if b <= 0:
                return 0.0
            # Recursive case: average over the four operations
            return 0.25 * sum(dp(max(a - da, 0), max(b - db, 0)) for da, db in ops)

        # Compute the probability for the scaled amounts
        return dp(m, m)

    soupServings = soup_servings
