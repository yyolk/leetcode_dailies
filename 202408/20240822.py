# https://leetcode.com/problems/number-complement/


class Solution:
    """476. Number Complement

    The **complement** of an integer is the integer you get when you flip all the `0`'s
    to `1`'s and all the `1`'s to `0`'s in its binary representation.

    * For example, The integer `5` is `"101"` in binary and its **complement** is
    `"010"` which is the integer `2`.

    Given an integer `num`, return *its complement*.

    """

    def find_complement(self, num: int) -> int:
        # Step 1: Calculate the bit length of num
        bit_length = num.bit_length()

        # Step 2: Create a mask with all bits set to 1 of the same length as num
        mask = (1 << bit_length) - 1

        # Step 3: XOR num with the mask to get the complement
        return num ^ mask

    findComplement = find_complement
