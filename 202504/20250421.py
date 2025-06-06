# https://leetcode.com/problems/count-the-hidden-sequences/


class Solution:
    """2145. Count the Hidden Sequences

    You are given a **0-indexed** array of `n` integers `differences`, which describes
    the **differences** between each pair of **consecutive** integers of a **hidden**
    sequence of length `(n + 1)`. More formally, call the hidden sequence `hidden`, then
    we have that `differences[i] = hidden[i + 1] - hidden[i]`.

    You are further given two integers `lower` and `upper` that describe the
    **inclusive** range of values `[lower, upper]` that the hidden sequence can contain.

    * For example, given `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`, the
    hidden sequence is a sequence of length `4` whose elements are in between `1` and
    `6` (**inclusive**).

      + `[3, 4, 1, 5]` and `[4, 5, 2, 6]` are possible hidden sequences.

      + `[5, 6, 3, 7]` is not possible since it contains an element greater than `6`.

      + `[1, 2, 3, 4]` is not possible since the differences are not correct.

    Return *the number of **possible** hidden sequences there are.* If there are no
    possible sequences, return `0`."""

    def number_of_arrays(self, differences: list[int], lower: int, upper: int) -> int:
        # Initialize variables to track the current prefix sum and its min/max values
        current_prefix = 0
        min_prefix = 0
        max_prefix = 0

        # Compute prefix sums and track their minimum and maximum
        for diff in differences:
            current_prefix += diff
            min_prefix = min(min_prefix, current_prefix)
            max_prefix = max(max_prefix, current_prefix)

        # Calculate the bounds for the starting value h[0]
        L = lower - min_prefix
        U = upper - max_prefix

        # Return the number of possible integer values for h[0]
        return max(0, U - L + 1)

    numberOfArrays = number_of_arrays
