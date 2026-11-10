# https://leetcode.com/problems/climbing-stairs-ii/


class Solution:
    """3693. Climbing Stairs II

    You are climbing a staircase with n + 1 steps, numbered from 0 to n.

    You are also given a 1-indexed integer array costs of length n, where
    costs[i] is the cost of step i.

    From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost
    of jumping from step i to step j is defined as: costs[j] + (j - i)^2

    You start from step 0 with cost = 0.

    Return the minimum total cost to reach step n.

    Constraints:

    * 1 <= n == costs.length <= 10^5
    * 1 <= costs[i] <= 10^4
    """

    def climb_stairs(self, n: int, costs: list[int]) -> int:
        # Min cost to reach each step; start at step 0 with cost 0.
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for jump in (1, 2, 3):
                j = i + jump
                if j > n:
                    break
                # Jump cost: target step cost + squared distance.
                cost = costs[j - 1] + jump * jump
                if dp[i] + cost < dp[j]:
                    dp[j] = dp[i] + cost
        return dp[n]

    climbStairs = climb_stairs
