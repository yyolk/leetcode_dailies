# https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution:
    """3345. Smallest Divisible Digit Product I
    
    You are given two integers `n` and `t`. Return the **smallest** number
    greater than or equal to `n` such that the **product of its digits** is
    divisible by `t`.
    Constraints:
    * `1 <= n <= 100`
    * `1 <= t <= 10`
    """
    def smallest_number(self, n: int, t: int) -> int:
        # Start checking from n upwards for the smallest valid number
        current = n
        while True:
            # Compute the product of the digits of current
            product = 1
            temp = current
            while temp > 0:
                # Multiply by the next digit
                product *= temp % 10
                # Early exit if product is already 0 (divisible by any t)
                if product == 0:
                    break
                temp //= 10
            # Return if product is divisible by t
            if product % t == 0:
                return current
            # Try the next number
            current += 1

    smallestNumber = smallest_number
