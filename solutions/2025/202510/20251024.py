# https://leetcode.com/problems/next-greater-numerically-balanced-number/


class Solution:
    """2048. Next Greater Numerically Balanced Number

    An integer `x` is **numerically balanced** if for every digit `d` in the number `x`,
    there are **exactly** `d` occurrences of that digit in `x`.

    Given an integer `n`, return *the **smallest numerically balanced** number
    **strictly greater** than* `n`*.*"""

    def next_beautiful_number(self, n: int) -> int:
        # Start checking from the integer immediately following n
        x = n + 1
        while True:
            # Convert the current number to a string for digit analysis
            s = str(x)
            # Initialize a frequency array for digits 0 through 9
            freq = [0] * 10
            # Count occurrences of each digit in the number
            for c in s:
                d = int(c)
                freq[d] += 1
            # Flag to determine if the number is numerically balanced
            is_bal = True
            # Verify each digit that appears does so exactly 'd' times
            for d in range(10):
                if freq[d] > 0 and freq[d] != d:
                    is_bal = False
                    break
            # If balanced, return the number as it's the smallest greater than n
            if is_bal:
                return x
            # Increment to check the next integer
            x += 1

    nextBeautifulNumber = next_beautiful_number
