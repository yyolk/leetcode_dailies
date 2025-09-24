# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    """166. Fraction to Recurring Decimal

    Given two integers representing the `numerator` and `denominator` of a fraction,
    return *the fraction in string format*.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    If multiple answers are possible, return **any of them**.

    It is **guaranteed** that the length of the answer string is less than `104` for all
    the given inputs."""

    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator case
        if numerator == 0:
            return "0"
        
        # Determine sign of the result
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        
        # Work with absolute values
        abs_n, abs_d = abs(numerator), abs(denominator)
        
        # Compute integer part
        int_part = abs_n // abs_d
        
        # Compute initial remainder
        remainder = abs_n % abs_d
        
        # If no remainder, return integer part with sign
        if remainder == 0:
            return f"{sign}{int_part}"
        
        # Prepare to build decimal part
        decimal = []
        seen = {}  # Map remainder to position in decimal
        
        # Process fractional part
        while remainder != 0 and remainder not in seen:
            # Record position for this remainder
            seen[remainder] = len(decimal)
            
            # Multiply remainder by 10 for next digit
            remainder *= 10
            
            # Append next digit
            digit = remainder // abs_d
            decimal.append(str(digit))
            
            # Update remainder
            remainder %= abs_d
        
        # If remainder is zero, decimal terminates
        if remainder == 0:
            decimal_str = "".join(decimal)
        else:
            # Insert parentheses for repeating part
            start = seen[remainder]
            decimal_str = "".join(decimal[:start]) + "(" + "".join(decimal[start:]) + ")"
        
        # Combine all parts
        return f"{sign}{int_part}.{decimal_str}"

    fractionToDecimal = fraction_to_decimal
