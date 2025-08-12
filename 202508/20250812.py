# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/


class Solution:
    """2787. Ways to Express an Integer as Sum of Powers

    Given two **positive** integers `n` and `x`.

    Return *the number of ways* `n` *can be expressed as the sum of the* `xth` *power of
    **unique** positive integers, in other words, the number of sets of unique integers*
    `[n1, n2, ..., nk]` *where* `n = n1x + n2x + ... + nkx`*.*

    Since the result can be very large, return it modulo `109 + 7`.

    For example, if `n = 160` and `x = 3`, one way to express `n` is `n = 23 + 33 + 53`.
    """

    def number_of_ways(self, n: int, x: int) -> int: ...

    numberOfWays = number_of_ways
