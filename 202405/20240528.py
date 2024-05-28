# https://leetcode.com/problems/get-equal-substrings-within-budget/


class Solution:
    """1208. Get Equal Substrings Within Budget

    You are given two strings `s` and `t` of the same length and an integer `max_cost`.

    You want to change `s` to `t`. Changing the `ith` character of `s` to `ith`
    character of `t` costs `|s[i] - t[i]|` (i.e., the absolute difference between the
    ASCII values of the characters).

    Return *the maximum length of a substring of* `s` *that can be changed to be the
    same as the corresponding substring of* `t` *with a cost less than or equal to*
    `max_cost`. If there is no substring from `s` that can be changed to its
    corresponding substring from `t`, return `0`.

    """

    def equal_substring(self, s: str, t: str, max_cost: int) -> int: ...

    equalSubstring = equal_substring
