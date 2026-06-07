# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/


class Solution:
    """3307. Find the K-th Character in String Game II

    Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

    You are given a **positive** integer `k`. You are also given an integer array
    `operations`, where `operations[i]` represents the **type** of the `ith` operation.

    Now Bob will ask Alice to perform **all** operations in sequence:

    * If `operations[i] == 0`, **append** a copy of `word` to itself.

    * If `operations[i] == 1`, generate a new string by **changing** each character in
    `word` to its **next** character in the English alphabet, and **append** it to the
    *original* `word`. For example, performing the operation on `"c"` generates `"cd"`
    and performing the operation on `"zb"` generates `"zbac"`.

    Return the value of the `kth` character in `word` after performing all the
    operations.

    **Note** that the character `"z"` can be changed to `"a"` in the second type of
    operation."""

    def kth_character(self, k: int, operations: list[int]) -> str:
        # Initialize a mask to track which operations involve shifting
        shift_mask = 0
        # Iterate over bit positions up to the number of bits needed to represent (k-1)
        for bit_position in range((k - 1).bit_length()):
            # Update the mask by setting the bit if the operation is a shift (1), else contribute 0
            shift_mask |= operations[bit_position] << bit_position
        # Compute the total number of shifts by counting set bits in the intersection of (k-1) and shift_mask
        total_shifts = ((k - 1) & shift_mask).bit_count()
        # Calculate the final character by shifting 'a' by the total number of shifts, wrapping around after 26
        final_character = chr(97 + (total_shifts % 26))
        # Return the resulting character
        return final_character

    kthCharacter = kth_character
