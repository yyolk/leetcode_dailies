# https://leetcode.com/problems/count-vowel-strings-in-ranges/


class Solution:
    """2559. Count Vowel Strings in Ranges

    You are given a **0-indexed** array of strings `words` and a 2D array of integers
    `queries`.

    Each query `queries[i] = [li, ri]` asks us to find the number of strings present in
    the range `li` to `ri` (both **inclusive**) of `words` that start and end with a
    vowel.

    Return *an array* `ans` *of size* `queries.length`*, where* `ans[i]` *is the answer
    to the* `i`th *query*.

    **Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`."""

    def vowel_strings(
        self, words: list[str], queries: list[list[int]]
    ) -> list[int]: ...

    vowelStrings = vowel_strings
