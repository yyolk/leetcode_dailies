# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/


class Solution:
    """1621. Number of Sets of K Non-Overlapping Line Segments

    Given `n` points on a 1-D plane, where the `ith` point (from `0` to `n-1`)
    is at `x = i`, find the number of ways we can draw **exactly** `k`
    **non-overlapping** line segments such that each segment covers two or more
    points. The endpoints of each segment must have **integral coordinates**.
    The `k` line segments **do not** have to cover all `n` points, and they are
    **allowed** to share endpoints.

    Return *the number of ways we can draw* `k` *non-overlapping line
    segments*. Since this number can be huge, return it **modulo** `10^9 + 7`.

    Constraints:

    * `2 <= n <= 1000`
    * `1 <= k <= n-1`
    """

    def number_of_sets(self, n: int, k: int) -> int:
        # Combinatorial map: k segments of length >= 1 and k+1 gaps of
        # length >= 0 summing to n-1 units. After subtracting 1 from each
        # segment, this is C(n + k - 1, 2k) mod 10^9+7.
        mod = 10**9 + 7
        return self._comb(n + k - 1, 2 * k, mod)

    def _comb(self, n: int, r: int, mod: int) -> int:
        if r < 0 or r > n:
            return 0
        if r > n - r:
            r = n - r
        numer = 1
        denom = 1
        for i in range(1, r + 1):
            numer = numer * (n - r + i) % mod
            denom = denom * i % mod
        # Modular inverse via Fermat (mod is prime).
        return numer * pow(denom, mod - 2, mod) % mod

    numberOfSets = number_of_sets
