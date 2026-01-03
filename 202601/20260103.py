# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid


class Solution:
    """1411. Number of Ways to Paint N x 3 Grid

    You have a grid of size n x 3 and you want to paint each cell with one of
    three colors: Red, Yellow, or Green. No two adjacent cells (sharing a
    vertical or horizontal side) can have the same color.

    Given n (number of rows), return the number of ways modulo 10^9 + 7.
    """
    def num_of_ways(self, n: int) -> int:
        # ABA: rows with col1 == col3 != col2 (6 such valid colorings)
        # ABC: rows with all columns different colors (6 such valid colorings)
        aba = 6
        abc = 6
        MOD = 10**9 + 7

        # Iterate from row 1 to row n (loop runs n-1 times)
        for _ in range(n - 1):
            # New ABA endings: 3 choices from each old ABA, 2 from each old ABC
            new_aba = (aba * 3 + abc * 2) % MOD
            # New ABC endings: 2 choices from each old ABA, 2 from each old ABC
            new_abc = ((aba + abc) * 2) % MOD
            aba = new_aba
            abc = new_abc

        # Total valid grids for n rows
        return (aba + abc) % MOD

    numOfWays = num_of_ways