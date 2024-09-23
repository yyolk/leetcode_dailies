# https://leetcode.com/problems/extra-characters-in-a-string/


class Solution:
    """2707. Extra Characters in a String

    You are given a **0\\-indexed** string `s` and a dictionary of words `dictionary`.
    You have to break `s` into one or more **non\\-overlapping** substrings such that
    each substring is present in `dictionary`. There may be some **extra characters** in
    `s` which are not present in any of the substrings.

    Return *the **minimum** number of extra characters left over if you break up* `s`
    *optimally.*

    """

    def min_extra_char(self, s: str, dictionary: list[str]) -> int: ...

    minExtraChar = min_extra_char
