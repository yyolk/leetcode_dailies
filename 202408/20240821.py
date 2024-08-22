# https://leetcode.com/problems/strange-printer/


class Solution:
    """664. Strange Printer

    There is a strange printer with the following two special properties:

    * The printer can only print a sequence of **the same character** each time.

    * At each turn, the printer can print new characters starting from and ending at any
    place and will cover the original existing characters.

    Given a string `s`, return *the minimum number of turns the printer needed to print
    it*.

    """

    def strange_printer(self, s: str) -> int:
        # Length of the input string
        n = len(s)
        
        # Initialize the DP table with infinity to represent uncomputed states
        dp = [[float("inf")] * n for _ in range(n)]

        # Base case: it takes exactly 1 turn to print a single character
        for i in range(n):
            dp[i][i] = 1

        # Iterate over all possible lengths of substrings, starting from 2
        for l in range(2, n + 1):
            # Iterate over all possible starting indices of substrings of length l
            for i in range(n - l + 1):
                # Calculate the ending index j of the current substring
                j = i + l - 1
                # If the characters at the start and end of the substring are the same
                if s[i] == s[j]:
                    # No additional turn needed, so we can extend the previous result
                    dp[i][j] = dp[i][j - 1]
                else:
                    # Otherwise, try all possible partitions and take the minimum turns
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        # Return the result for the entire string
        return dp[0][n - 1]

    strangePrinter = strange_printer
