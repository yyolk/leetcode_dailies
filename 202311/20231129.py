# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    """191. Number of 1 Bits

    Write a function that takes the binary representation of an unsigned integer and
    returns the number of '1' bits it has (also known as the [Hamming
    weight](http://en.wikipedia.org/wiki/Hamming_weight)).

    **Note:**

    * Note that in some languages, such as Java, there is no unsigned integer type. In
    this case, the input will be given as a signed integer type. It should not affect
    your implementation, as the integer's internal binary representation is the same,
    whether it is signed or unsigned.

    * In Java, the compiler represents the signed integers using [2's complement
    notation](https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in **Example
    3**, the input represents the signed integer. `-3`.
    """

    def hamming_weight(self, n: int) -> int:
        """Finds the Hamming weight for an unsigned integer.

        Counts the number of '1' bits an unsigned integer has.

        Args:
            n: The unsigned integer.

        Returns:
            The number of '1' bits, aka the Hamming weight.
        """
        # Store the count of '1' bits
        count = 0

        # Iterate over each bit in a 32-bit integer
        for i in range(32):
            # Right shift n by i bits, then perform bitwise AND with 1 to check the
            # value of the current bit.
            # Increment the count if the current bit is 1
            count += (n >> i) & 1

        # Return the total count of '1' bits in the binary representation
        return count

    def alt_hamming_weight(self, n: int) -> int:
        """Alternative solution to finding hamming weight for the unsigned integer.

        Args:
            n: The unsigned integer.

        Returns:
            The number of '1' bits, aka the Hamming weight.
        """
        return bin(n).count("1")

    hammingWeight = hamming_weight
