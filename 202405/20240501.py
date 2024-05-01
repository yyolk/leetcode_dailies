# https://leetcode.com/problems/reverse-prefix-of-word/


class Solution:
    """2000. Reverse Prefix of Word

    Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of
    `word` that starts at index `0` and ends at the index of the **first occurrence** of
    `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

    * For example, if `word = "abcdefd"` and `ch = "d"`, then you should **reverse** the
    segment that starts at `0` and ends at `3` (**inclusive**). The resulting string
    will be `"dcbaefd"`.

    Return *the resulting string*.

    """

    def reverse_prefix(self, word: str, ch: str) -> str: ...

    reversePrefix = reverse_prefix
