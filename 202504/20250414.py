# https://leetcode.com/problems/count-good-triplets/


class Solution:
    """1534. Count Good Triplets

    Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to
    find the number of good triplets.

    A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are
    true:

    * `0 <= i < j < k < arr.length`

    * `|arr[i] - arr[j]| <= a`

    * `|arr[j] - arr[k]| <= b`

    * `|arr[i] - arr[k]| <= c`

    Where `|x|` denotes the absolute value of `x`.

    Return *the number of good triplets*."""

    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int: ...

    countGoodTriplets = count_good_triplets
