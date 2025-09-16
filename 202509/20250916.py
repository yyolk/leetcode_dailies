# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
from math import gcd


class Solution:
    """2197. Replace Non-Coprime Numbers in Array

    You are given an array of integers `nums`. Perform the following steps:

    1. Find **any** two **adjacent** numbers in `nums` that are **non-coprime**.

    2. If no such numbers are found, **stop** the process.

    3. Otherwise, delete the two numbers and **replace** them with their **LCM (Least
    Common Multiple)**.

    4. **Repeat** this process as long as you keep finding two adjacent non-coprime
    numbers.

    Return *the **final** modified array.* It can be shown that replacing adjacent non-
    coprime numbers in **any** arbitrary order will lead to the same result.

    The test cases are generated such that the values in the final array are **less than
    or equal** to `108`.

    Two values `x` and `y` are **non-coprime** if `GCD(x, y) > 1` where `GCD(x, y)` is
    the **Greatest Common Divisor** of `x` and `y`."""

    def replace_non_coprimes(self, nums: list[int]) -> list[int]:        
        # Helper function to compute LCM: a * b // gcd(a, b)
        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)
        
        # Use stack to efficiently merge adjacent non-coprime numbers
        stack = []
        
        for num in nums:
            # Append current number to stack
            stack.append(num)
            
            # Merge while the last two numbers are non-coprime (gcd > 1)
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                # Pop the last two numbers
                b = stack.pop()
                a = stack.pop()
                # Replace with their LCM
                stack.append(lcm(a, b))
        
        # Stack now holds the final modified array
        return stack

    replaceNonCoprimes = replace_non_coprimes
