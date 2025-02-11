# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/


class Solution:
    """1910. Remove All Occurrences of a Substring

    Given two strings `s` and `part`, perform the following operation on `s` until
    **all** occurrences of the substring `part` are removed:

    * Find the **leftmost** occurrence of the substring `part` and **remove** it from
    `s`.

    Return `s` *after removing all occurrences of* `part`.

    A **substring** is a contiguous sequence of characters in a string."""

    def remove_occurrences(self, s: str, part: str) -> str: ...

    removeOccurrences = remove_occurrences
