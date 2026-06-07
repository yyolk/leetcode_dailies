# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


class Solution:
    """1317. Convert Integer to the Sum of Two No-Zero Integers

    **No-Zero integer** is a positive integer that **does not contain any `0`** in its
    decimal representation.

    Given an integer `n`, return *a list of two integers* `[a, b]` *where*:

    * `a` and `b` are **No-Zero integers**.

    * `a + b = n`

    The test cases are generated so that there is at least one valid solution. If there
    are many valid solutions, you can return any of them."""

    def get_no_zero_integers(self, n: int) -> list[int]:
        # Helper function to check if a number contains no "0" in its string representation
        def has_no_zero(x: int) -> bool:
            return "0" not in str(x)

        # Iterate over possible values for "a" from 1 to n-1
        for a in range(1, n):
            # Calculate "b" as n - a
            b = n - a
            # Check if both "a" and "b" have no zeros
            if has_no_zero(a) and has_no_zero(b):
                # Return the pair if conditions are met
                return [a, b]

    getNoZeroIntegers = get_no_zero_integers
