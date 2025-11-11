# https://leetcode.com/problems/ones-and-zeroes/


class Solution:
    """474. Ones and Zeroes

    You are given an array of binary strings strs and two integers m and n.

    Return the size of the largest subset of strs such that there are at most m
    0's and n 1's in the subset.

    A set x is a subset of a set y if all elements of x are also elements of y.
    """
    def find_max_form(self, strs: list[str], m: int, n: int) -> int:
        # Initialize DP table: dp[i][j] will be max subset size with <=i zeros and <=j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            # Count zeros and ones in the string
            zeros = s.count('0')
            ones = len(s) - zeros

            # Update DP table in reverse order to avoid using same item multiple times
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # Either skip this string or take it if we have enough zeros and ones
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        # The answer is in dp[m][n]
        return dp[m][n]

    findMaxForm = find_max_form