# https://leetcode.com/problems/minimum-operations-to-sort-a-string/


class Solution:
    """3863. Minimum Operations to Sort a String

    You are given a string `s` consisting of lowercase English letters.

    In one operation, you can select any **substring** of `s` that is **not** the
    entire string and **sort** it in **non-descending alphabetical** order.

    Return the **minimum** number of operations required to make `s` sorted in
    **non-descending** order. If it is not possible, return -1.

    Constraints:

    * `1 <= s.length <= 105`

    * `s` consists of only lowercase English letters.
    """

    def min_operations(self, s: str) -> int:
        """Return the minimum operations to sort s via proper substring sorts.

        Args:
            s (str): Input string of lowercase English letters.

        Returns:
            int: Minimum operations needed, or -1 if impossible.
        """
        # Already non-decreasing: no operations required.
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            return 0
        # Unsorted length-2 string cannot be fixed; only single characters can
        # be sorted as proper substrings.
        if len(s) == 2:
            return -1
        # Global minimum and maximum characters.
        mn, mx = min(s), max(s)
        # First char is already the min, or last char is already the max:
        # sorting the complementary proper substring finishes the sort.
        if s[0] == mn or s[-1] == mx:
            return 1
        # An extreme appears in the interior: place it at an end, then finish.
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2
        # Only remaining case: max appears solely at the front and min solely
        # at the back. Requires three operations.
        return 3

    minOperations = min_operations
