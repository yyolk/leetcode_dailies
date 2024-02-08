# https://leetcode.com/problems/perfect-squares/


class Solution:
    """279. Perfect Squares

    Given an integer `n`, return *the least number of perfect square numbers that sum
    to* `n`.

    A **perfect square** is an integer that is the square of an integer; in other words,
    it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16`
    are perfect squares while `3` and `11` are not.

    """

    def num_squares(self, n: int) -> int:
        # Create a list to store the minimum number of perfect squares for each number up to n
        dp = [float('inf')] * (n + 1)
        
        # The minimum number of perfect squares for 0 is 0
        dp[0] = 0

        # Iterate through each number up to n
        for i in range(1, n + 1):
            # Iterate through each square number up to sqrt(i)
            j = 1
            while j * j <= i:
                # Update the minimum number of perfect squares needed for i
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        # The result is stored in dp[n]
        return dp[n]

    numSquares = num_squares
