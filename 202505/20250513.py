# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/


class Solution:
    """3335. Total Characters in String After Transformations I

    You are given a string `s` and an integer `t`, representing the number of
    **transformations** to perform. In one **transformation**, every character in `s` is
    replaced according to the following rules:

    * If the character is `'z'`, replace it with the string `"ab"`.

    * Otherwise, replace it with the **next** character in the alphabet. For example,
    `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

    Return the **length** of the resulting string after **exactly** `t` transformations.

    Since the answer may be very large, return it **modulo** `109 + 7`."""

    def length_after_transformations(self, s: str, t: int) -> int: ...

    lengthAfterTransformations = length_after_transformations
