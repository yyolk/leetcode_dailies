# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/


class Solution:
    """3405. Count the Number of Arrays with K Matching Adjacent Elements

    You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is
    defined as follows:

    * Each element in `arr` is in the **inclusive** range `[1, m]`.

    * *Exactly* `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1]
    == arr[i]`.

    Return the number of **good arrays** that can be formed.

    Since the answer may be very large, return it **modulo** `109 + 7`."""

    def count_good_arrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        # Calculate the number of good arrays:
        # - m: choices for the first element (any value from 1 to m)
        # - (m-1)^(n-k-1): for the n-k-1 positions where arr[i] != arr[i-1], choose from (m-1) values
        # - comb(n-1, k): number of ways to choose k positions out of n-1 for equal adjacent pairs
        # - Apply modulo to keep the result within bounds
        return m * pow(m - 1, n - k - 1, mod) * comb(n - 1, k) % mod

    countGoodArrays = count_good_arrays
