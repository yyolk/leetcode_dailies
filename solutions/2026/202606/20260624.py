# https://leetcode.com/problems/number-of-zigzag-arrays-ii/


class Solution:
    """3700. Number of ZigZag Arrays II

    You are given three integers `n`, `l`, and `r`.

    A **ZigZag** array of length `n` is defined as follows:

    * Each element lies in the range `[l, r]`.

    * No **two** adjacent elements are equal.

    * No **three** consecutive elements form a **strictly increasing** or **strictly
    decreasing** sequence.

    Return the total number of valid **ZigZag** arrays.

    Since the answer may be large, return it **modulo** `109 + 7`.

    A **sequence** is said to be **strictly increasing** if each element is strictly
    greater than its previous one (if exists).

    A **sequence** is said to be **strictly decreasing** if each element is strictly
    smaller than its previous one (if exists).

    Constraints:

    * `3 <= n <= 109`

    * `1 <= l < r <= 75`\u200b\u200b\u200b\u200b\u200b\u200b\u200b"""

    def zig_zag_arrays(self, n: int, l: int, r: int) -> int: ...

    zigZagArrays = zig_zag_arrays
