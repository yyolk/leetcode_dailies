# https://leetcode.com/problems/count-commas-in-range-ii/


class Solution:
    """3871. Count Commas in Range II

    You are given an integer `n`.

    Return the **total** number of commas used when writing all integers from
    `[1, n]` (inclusive) in **standard** number formatting.

    In **standard** formatting:

    * A comma is inserted after **every three** digits from the right.

    * Numbers with **fewer** than 4 digits contain no commas.

    Constraints:

    * `1 <= n <= 10^15`
    """

    def count_commas(self, n: int) -> int:
        # Each threshold 10^(3k) adds one more comma to every number >= that value.
        # Accumulate the contribution of each new comma level up to n.
        ans = 0
        x = 1000
        while x <= n:
            ans += n - x + 1
            x *= 1000
        return ans

    countCommas = count_commas
