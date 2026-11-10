# https://leetcode.com/problems/climbing-stairs-ii/


class Solution:
    """3693. Climbing Stairs II

    You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

    You are also given a **1-indexed** integer array `costs` of length `n`, where
    `costs[i]` is the cost of step `i`.

    From step `i`, you can jump **only** to step `i + 1`, `i + 2`, or `i + 3`. The cost
    of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)2`

    You start from step 0 with `cost = 0`.

    Return the **minimum** total cost to reach step `n`.

    Constraints:

    * `1 <= n == costs.length <= 105\u200b\u200b\u200b\u200b\u200b\u200b\u200b`

    * `1 <= costs[i] <= 104`"""

    def climb_stairs(self, n: int, costs: list[int]) -> int:
        """...

        Proposed solution ...

        Args:
            n (int): ...
            costs (list of int): ...

        Returns:
            int: ..."""
        ...

    climbStairs = climb_stairs
