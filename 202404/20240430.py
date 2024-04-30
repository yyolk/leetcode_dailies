# https://leetcode.com/problems/number-of-wonderful-substrings/


class Solution:
    """1915. Number of Wonderful Substrings

    A **wonderful** string is a string where **at most one** letter appears an **odd**
    number of times.

    * For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

    Given a string `word` that consists of the first ten lowercase English letters
    (`'a'` through `'j'`), return *the **number of wonderful non-empty substrings** in*
    `word`*. If the same substring appears multiple times in* `word`*, then count **each
    occurrence** separately.*

    A **substring** is a contiguous sequence of characters in a string.

    """

    def wonderful_substrings(self, word: str) -> int: ...

    wonderfulSubstrings = wonderful_substrings
