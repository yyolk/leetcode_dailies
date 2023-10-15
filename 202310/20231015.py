# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
MOD = 10**9 + 7  # Our ceiling for the answer to avoid integer overflow


class Solution:
    """1269. Number of Ways to Stay in the Same Place After Some Steps

    You have a pointer at index `0` in an array of size `arrLen`. At each step, you can
    move 1 position to the left, 1 position to the right in the array, or stay in the
    same place (The pointer should not be placed outside the array at any time).

    Given two integers `steps` and `arrLen`, return the number of ways such that your
    pointer is still at index `0` after **exactly** `steps` steps. Since the answer may
    be too large, return it **modulo** `109 + 7`.
    """

    def num_ways(self, steps: int, arr_len: int) -> int:
        """Number of ways to stay in the same place after the steps.

        Proposed solution using dynamic programming.

        Args:
            steps (int): The number of steps.
            arr_len (int): The size of the array we're stepping through.

        Returns:
            int: The number of ways to stay in the same place after "steps" steps.
        """
        # Calculate the max position you can reach based on steps and arr_len
        max_pos = min(steps // 2, arr_len - 1)

        # Initialize a 2D array to store the number of ways to reach each position
        dp = [[0] * (max_pos + 1) for _ in range(steps + 1)]

        # Initialize the starting position at index 0 with 1 way
        dp[0][0] = 1

        # Iterate over the number of steps
        for i in range(1, steps + 1):
            # Iterate over positions up to the max position
            for j in range(max_pos + 1):
                # Update the number of ways to reach the current position

                # Stay in the same position
                dp[i][j] = dp[i - 1][j]

                # If the current position is not at the leftmost boundary,
                # a left step is possible
                if j > 0:
                    # Move one position to the left
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

                # If the current position is not at the rightmost boundary,
                # a right step is possible
                if j < max_pos:
                    # Move one position to the right
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD

        # The answer is the number of ways to reach index 0 after "steps" steps
        return dp[steps][0]

    # I'm a snake_case maximalist
    numWays = num_ways
