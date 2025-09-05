# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/


class Solution:
    """2749. Minimum Operations to Make the Integer Zero

    You are given two integers `num1` and `num2`.

    In one operation, you can choose integer `i` in the range `[0, 60]` and subtract `2i
    + num2` from `num1`.

    Return *the integer denoting the **minimum** number of operations needed to make*
    `num1` *equal to* `0`.

    If it is impossible to make `num1` equal to `0`, return `-1`."""

    def make_the_integer_zero(self, num1: int, num2: int) -> int: ...

    makeTheIntegerZero = make_the_integer_zero
