# https://leetcode.com/problems/sequential-digits/


class Solution:
    """1291. Sequential Digits

    An integer has sequential digits if and only if each digit in the number is one
    more than the previous digit. Return a sorted list of all the integers in the
    range [low, high] inclusive that have sequential digits.

    Constraints:
    * 10 <= low <= high <= 10^9"""

    def sequential_digits(self, low: int, high: int) -> list[int]:
        result = []
        # Generate all sequential numbers by each possible start digit 1-9
        for start in range(1, 10):
            num = start
            # Append consecutive digits to build longer numbers (2-9 digits)
            for d in range(start + 1, 10):
                num = num * 10 + d  # left-shift existing digits and append next
                if num > high:
                    break  # remaining extensions of this start exceed high
                if num >= low:
                    result.append(num)
        result.sort()  # numbers generated out-of-order across start digits
        return result

    sequentialDigits = sequential_digits
