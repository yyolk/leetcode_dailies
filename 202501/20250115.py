# https://leetcode.com/problems/minimize-xor/


class Solution:
    """2429. Minimize XOR

    Given two positive integers `num1` and `num2`, find the positive integer `x` such
    that:

    * `x` has the same number of set bits as `num2`, and

    * The value `x XOR num1` is **minimal**.

    Note that `XOR` is the bitwise XOR operation.

    Return *the integer* `x`. The test cases are generated such that `x` is **uniquely
    determined**.

    The number of **set bits** of an integer is the number of `1`'s in its binary
    representation."""

    def minimize_xor(self, num1: int, num2: int) -> int:
        diff_set_bits = num1.bit_count() - num2.bit_count()
        if diff_set_bits > 0:
            # Reset the "diff_set_bits" least significant bits of the number "num1"
            for _ in range(diff_set_bits):
                num1 &= num1 - 1
        else:
            # Set the "diff_set_bits" least insignificant bits of the number "num1"
            for _ in range(-diff_set_bits):  
                num1 |= num1 + 1   
        return num1

    minimizeXor = minimize_xor
