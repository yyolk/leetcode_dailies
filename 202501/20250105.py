# https://leetcode.com/problems/shifting-letters-ii/


class Solution:
    """2381. Shifting Letters II

    You are given a string `s` of lowercase English letters and a 2D integer array
    `shifts` where `shifts[i] = [starti, endi, directioni]`. For every `i`, **shift**
    the characters in `s` from the index `starti` to the index `endi` (**inclusive**)
    forward if `directioni = 1`, or shift the characters backward if `directioni = 0`.

    Shifting a character **forward** means replacing it with the **next** letter in the
    alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a
    character **backward** means replacing it with the **previous** letter in the
    alphabet (wrapping around so that `'a'` becomes `'z'`).

    Return *the final string after all such shifts to* `s` *are applied*."""

    def shifting_letters(self, s: str, shifts: list[list[int]]) -> str: ...

    shiftingLetters = shifting_letters
