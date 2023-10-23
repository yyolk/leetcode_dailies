# https://leetcode.com/problems/power-of-four/


class Solution:
    """342. Power of Four

    Given an integer `n`, return *`true` if it is a power of four. Otherwise, return
    `false`*.

    An integer `n` is a power of four, if there exists an integer `x` such that `n ==
    4x`.
    """

    def is_power_of_four(self, n: int) -> bool:
        """Is number a power of four?

        Proposed solution, uses binary representation of the input and bit counting
        the bits to determine.

        Args:
            n (int): Input integer to determine if it's a power of four.

        Returns:
            bool: True if n is power of four.
        """
        # Check if n is a positive integer
        if n <= 0:
            return False

        # Check if there is only one '1' bit in the binary representation
        binary_representation = bin(n)
        return (
            binary_representation.count("1") == 1
            and binary_representation.count("0") % 2 == 1
        )

    isPowerOfFour = is_power_of_four
