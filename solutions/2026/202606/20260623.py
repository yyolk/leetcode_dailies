# https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution:
    """3699. Number of ZigZag Arrays I

    You are given three integers n, l, and r. A ZigZag array of length n
    has each element in [l,r], no adjacent equal, and no three consecutive
    strictly increasing or decreasing. Return the count mod 10^9+7.
    """
    def zig_zag_arrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        # up[j], down[j]: ways ending at rank j (1..m) with last step inc/dec
        up = [0] * (m + 2)
        down = [0] * (m + 2)
        for j in range(1, m + 1):
            up[j] = j - 1
            down[j] = m - j
        # extend n-2 times from length 2 enforcing flip each step
        for _ in range(n - 2):
            # prefix sums of current down for sum of smaller prev
            prefix_down = [0] * (m + 2)
            for j in range(1, m + 1):
                prefix_down[j] = (prefix_down[j - 1] + down[j]) % MOD
            # suffix sums of current up for sum of larger prev
            suffix_up = [0] * (m + 2)
            for j in range(m, 0, -1):
                suffix_up[j] = (suffix_up[j + 1] + up[j]) % MOD
            for j in range(1, m + 1):
                # new up at j: from prior down + prev < j
                up[j] = prefix_down[j - 1]
                # new down at j: from prior up + prev > j
                down[j] = suffix_up[j + 1]
        # sum ways over all possible endings at length n
        total = 0
        for j in range(1, m + 1):
            total = (total + up[j] + down[j]) % MOD
        return total

    zigZagArrays = zig_zag_arrays