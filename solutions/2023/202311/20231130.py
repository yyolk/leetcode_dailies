# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/


class Solution:
    """1611. Minimum One Bit Operations to Make Integers Zero

    Given an integer `n`, you must transform it into `0` using the following operations
    any number of times:

    * Change the rightmost (`0th`) bit in the binary representation of `n`.

    * Change the `ith` bit in the binary representation of `n` if the `(i-1)th` bit is
    set to `1` and the `(i-2)th` through `0th` bits are set to `0`.

    Return *the minimum number of operations to transform* `n` *into* `0`*.*
    """

    def minimum_one_bit_operations(self, n: int) -> int:
        """The minimium number of one bit operations to change input n to 0.

        Proposed solution using Gray Code conversion.

        Gray Code is a binary numeral system in which two successive values differ in
        only one bit. https://en.wikipedia.org/wiki/Gray_code

        Args:
            n: Input integer to transform into 0.

        Returns:
            Minimum number of operations to change n to 0.
        """
        operations = 0

        # Continue the loop until n becomes 0.
        while n:
            # Calculate the bitwise XOR of n and its predecessor (n - 1).
            xor_result = n ^ (n - 1)

            # Update the operations count by negating the result of the XOR operation
            # and subtracting it from the current value of operations.
            operations = -operations - xor_result

            # Remove the rightmost set bit by performing a bitwise AND operation
            # with the result of subtracting 1 from n.
            n &= n - 1

        # Return the aboslute value of operations as the minimum number of operations.
        return abs(operations)

    minimumOneBitOperations = minimum_one_bit_operations
