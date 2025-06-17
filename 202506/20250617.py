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

    def count_good_arrays(self, n: int, m: int, k: int) -> int: ...

    countGoodArrays = count_good_arrays
