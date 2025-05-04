# https://leetcode.com/problems/number-of-equivalent-domino-pairs/


class Solution:
    """1128. Number of Equivalent Domino Pairs

    Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j]
    = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`)
    - that is, one domino can be rotated to be equal to another domino.

    Return *the number of pairs* `(i, j)` *for which* `0 <= i < j < dominoes.length`*,
    and* `dominoes[i]` *is **equivalent to*** `dominoes[j]`."""

    def num_equiv_domino_pairs(self, dominoes: list[list[int]]) -> int: ...

    numEquivDominoPairs = num_equiv_domino_pairs
