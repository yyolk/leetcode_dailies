# https://leetcode.com/problems/maximum-product-of-two-digits/


class Solution:
    """3536. Maximum Product of Two Digits

    You are given a positive integer `n`.
    Return the **maximum** product of any two digits in `n`.

    **Note:** You may use the **same** digit twice if it
    appears more than once in `n`.

    Constraints:
    * `10 <= n <= 10^9`
    """

    def max_product(self, n: int) -> int:
        # Track the largest and second-largest digits found
        max1 = max2 = 0
        # Extract digits one by one from the least significant
        while n:
            digit = n % 10
            if digit > max1:
                # New maximum found; demote previous max1 to max2
                max2 = max1
                max1 = digit
            elif digit > max2:
                # Update second max if larger than current max2
                max2 = digit
            n //= 10
        # Product of the two largest digits
        return max1 * max2

    maxProduct = max_product
