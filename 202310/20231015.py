# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/


class Solution:
    """1269. Number of Ways to Stay in the Same Place After Some Steps

    You have a pointer at index `0` in an array of size `arrLen`. At each step, you can
    move 1 position to the left, 1 position to the right in the array, or stay in the
    same place (The pointer should not be placed outside the array at any time).

    Given two integers `steps` and `arrLen`, return the number of ways such that your
    pointer is still at index `0` after **exactly** `steps` steps. Since the answer may
    be too large, return it **modulo** `109 + 7`.
    """

    def numWays(self, steps: int, arrLen: int) -> int:
        ...
