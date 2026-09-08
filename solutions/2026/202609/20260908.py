# https://leetcode.com/problems/count-commas-in-range/


class Solution:
    """3870. Count Commas in Range

    You are given an integer `n`.

    Return the **total** number of commas used when writing all integers from
    `[1, n]` (inclusive) in **standard** number formatting.

    In **standard** formatting:

    * A comma is inserted after **every three** digits from the right.

    * Numbers with **fewer** than 4 digits contain no commas.

    Constraints:

    * `1 <= n <= 10^5`
    """

    def count_commas(self, n: int) -> int:
        # Numbers 1..999 have no commas; each from 1000 onward has exactly one.
        return max(0, n - 999)

    countCommas = count_commas
