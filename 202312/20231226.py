# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
MOD = 10**9 + 7


class Solution:
    """1155. Number of Dice Rolls With Target Sum

    You have `n` dice, and each die has `k` faces numbered from `1` to `k`.

    Given three integers `n`, `k`, and `target`, return *the number of possible ways
    (out of the* `kn` *total ways)* *to roll the dice, so the sum of the face-up numbers
    equals* `target`. Since the answer may be too large, return it **modulo** `109 + 7`.
    """

    def num_rolls_to_target(self, n: int, k: int, target: int) -> int:
        # Use dynamic programming - dp[i][j]: number of ways to get sum j using i dice.
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for face in range(1, k + 1):
                    # Check if the current face value is valid for the current target sum.
                    if j - face >= 0:
                        # Accumulate the ways to get the current sum using the current face value.
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        return dp[n][target]

    numRollsToTarget = num_rolls_to_target
