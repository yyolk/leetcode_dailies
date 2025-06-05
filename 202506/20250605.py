# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/


class Solution:
    """1061. Lexicographically Smallest Equivalent String

    You are given two strings of the same length `s1` and `s2` and a string `base_str`.

    We say `s1[i]` and `s2[i]` are equivalent characters.

    * For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a' == 'c'`, `'b' ==
    'd'`, and `'c' == 'e'`.

    Equivalent characters follow the usual rules of any equivalence relation:

    * **Reflexivity:** `'a' == 'a'`.

    * **Symmetry:** `'a' == 'b'` implies `'b' == 'a'`.

    * **Transitivity:** `'a' == 'b'` and `'b' == 'c'` implies `'a' == 'c'`.

    For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`,
    `"acd"` and `"aab"` are equivalent strings of `base_str = "eed"`, and `"aab"` is the
    lexicographically smallest equivalent string of `base_str`.

    Return *the lexicographically smallest equivalent string of* `base_str` *by using
    the equivalency information from* `s1` *and* `s2`."""

    def smallest_equivalent_string(self, s1: str, s2: str, base_str: str) -> str: ...

    smallestEquivalentString = smallest_equivalent_string
