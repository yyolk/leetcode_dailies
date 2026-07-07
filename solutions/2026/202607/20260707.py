# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/


class Solution:
    """3754. Concatenate Non-Zero Digits and Multiply by Sum I

    You are given an integer `n`.

    Form a new integer `x` by concatenating all the **non-zero digits** of `n` in their
    original order. If there are no **non-zero** digits, `x = 0`.

    Let `sum` be the **sum of digits** in `x`.

    Return an integer representing the value of `x * sum`.

    Constraints:

    * `0 <= n <= 109`"""

    def sum_and_multiply(self, n: int) -> int: ...

    sumAndMultiply = sum_and_multiply
