# https://leetcode.com/problems/count-the-number-of-ideal-arrays/


class Solution:
    """2338. Count the Number of Ideal Arrays

    You are given two integers `n` and `max_value`, which are used to describe an
    **ideal** array.

    A **0-indexed** integer array `arr` of length `n` is considered **ideal** if the
    following conditions hold:

    * Every `arr[i]` is a value from `1` to `max_value`, for `0 <= i < n`.

    * Every `arr[i]` is divisible by `arr[i - 1]`, for `0 < i < n`.

    Return *the number of **distinct** ideal arrays of length* `n`. Since the answer may
    be very large, return it modulo `109 + 7`."""

    def ideal_arrays(self, n: int, max_value: int) -> int: ...

    idealArrays = ideal_arrays
