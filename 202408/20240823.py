# https://leetcode.com/problems/fraction-addition-and-subtraction/
from math import gcd


class Solution:
    """592. Fraction Addition and Subtraction

    Given a string `expression` representing an expression of fraction addition and
    subtraction, return the calculation result in string format.

    The final result should be an [irreducible
    fraction](https://en.wikipedia.org/wiki/Irreducible_fraction). If your final result
    is an integer, change it to the format of a fraction that has a denominator `1`. So
    in this case, `2` should be converted to `2/1`.

    """

    def fraction_addition(self, expression: str) -> str:
        # Helper function to add two fractions
        def add_fractions(num1, den1, num2, den2):
            numerator = num1 * den2 + num2 * den1
            denominator = den1 * den2
            common_divisor = gcd(abs(numerator), denominator)
            return numerator // common_divisor, denominator // common_divisor
        
        # Parse the expression and initialize result as 0/1
        fractions = expression.replace('-', '+-').split('+')
        result_num, result_den = 0, 1
        
        for fraction in fractions:
            if fraction:
                num, den = map(int, fraction.split('/'))
                result_num, result_den = add_fractions(result_num, result_den, num, den)
        
        # If result is 0, return "0/1"
        if result_num == 0:
            return "0/1"
        
        return f"{result_num}/{result_den}"

    fractionAddition = fraction_addition
