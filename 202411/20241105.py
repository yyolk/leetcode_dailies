# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/


class Solution:
    """2914. Minimum Number of Changes to Make Binary String Beautiful

    You are given a **0\\-indexed** binary string `s` having an even length.

    A string is **beautiful** if it's possible to partition it into one or more
    substrings such that:

    * Each substring has an **even length**.

    * Each substring contains **only** `1`'s or **only** `0`'s.

    You can change any character in `s` to `0` or `1`.

    Return *the **minimum** number of changes required to make the string* `s`
    *beautiful*.

    """

    def min_changes(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s), 2):
            # Check if the current pair is not already beautiful (either both '0' or both '1')
            if s[i] != s[i + 1]:
                # We need at least one change per mismatched pair
                changes += 1

        return changes

    minChanges = min_changes
