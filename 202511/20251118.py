# https://leetcode.com/problems/1-bit-and-2-bit-characters/


class Solution:
    """717. 1-bit and 2-bit Characters

    We have two special characters:

    - The first character can be represented by one bit 0.
    - The second character can be represented by two bits (10 or 11).

    Given a binary array bits that ends with 0, return true if the last
    character must be a one-bit character.
    """
    def is_one_bit_character(self, bits: list[int]) -> bool:
        # Initialize starting index
        i = 0
        # Cache the length for repeated checks
        n = len(bits)
        # Parse the bits greedily until the second-to-last index
        while i < n - 1:
            # If bit is 1, consume two bits for a two-bit character
            if bits[i] == 1:
                i += 2
            # Otherwise, consume one bit for a one-bit character
            else:
                i += 1
        # Last character is one-bit if parsing stopped at the last index
        return i == n - 1

    isOneBitCharacter = is_one_bit_character