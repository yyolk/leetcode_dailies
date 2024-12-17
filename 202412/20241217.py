# https://leetcode.com/problems/construct-string-with-repeat-limit/


class Solution:
    """2182. Construct String With Repeat Limit

    You are given a string `s` and an integer `repeat_limit`. Construct a new string
    `repeat_limitedString` using the characters of `s` such that no letter appears
    **more than** `repeat_limit` times **in a row**. You do **not** have to use all
    characters from `s`.

    Return *the **lexicographically largest*** `repeat_limitedString` *possible*.

    A string `a` is **lexicographically larger** than a string `b` if in the first
    position where `a` and `b` differ, string `a` has a letter that appears later in the
    alphabet than the corresponding letter in `b`. If the first `min(a.length,
    b.length)` characters do not differ, then the longer string is the lexicographically
    larger one."""

    def repeat_limited_string(self, s: str, repeat_limit: int) -> str: ...

    repeatLimitedString = repeat_limited_string
