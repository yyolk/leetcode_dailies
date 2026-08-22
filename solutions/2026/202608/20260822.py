# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/


class Solution:
    """3622. Check Divisibility by Digit Sum and Product

    You are given a positive integer `n`. Determine whether `n` is divisible by the
    **sum** of the following two values:

    * The **digit sum** of `n` (the sum of its digits).

    * The **digit** **product** of `n` (the product of its digits).

    Return `true` if `n` is divisible by this sum; otherwise, return `false`.

    Constraints:

    * `1 <= n <= 106`"""

    def check_divisibility(self, n: int) -> bool:
        """Return whether n is divisible by digit-sum(n) + digit-product(n)."""
        digit_sum = 0
        digit_product = 1
        value = n

        while value > 0:
            value, digit = divmod(value, 10)
            digit_sum += digit
            digit_product *= digit

        return n % (digit_sum + digit_product) == 0

    checkDivisibility = check_divisibility
