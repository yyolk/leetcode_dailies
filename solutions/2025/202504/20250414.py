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

    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        # Iterate over all possible i, j, k where i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # Check all three conditions
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        count += 1
        return count

    countGoodTriplets = count_good_triplets
