# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    """1137. N-th Tribonacci Number

    The Tribonacci sequence Tn is defined as follows:

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given `n`, return the value of Tn.

    """

    def tribonacci(self, n: int) -> int:
        # Base cases: T0 = 0, T1 = 1, T2 = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize a DP array to store Tribonacci numbers
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1

        # Compute Tribonacci numbers from T3 to Tn
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        # Return the calculated Tribonacci number for n
        return dp[n]