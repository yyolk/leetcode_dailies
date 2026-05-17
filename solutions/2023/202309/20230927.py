# https://leetcode.com/problems/decoded-string-at-index/


class Solution:
    """880. Decoded String at Index

    You are given an encoded string `s`. To decode the string to a tape, the encoded string
    is read one character at a time and the following steps are taken:

    * If the character read is a letter, that letter is written onto the tape.

    * If the character read is a digit `d`, the entire current tape is repeatedly written `d
    - 1` more times in total.

    Given an integer `k`, return *the* `kth` *letter (**1-indexed)** in the decoded string*.
    """

    def decodeAtIndex(self, s: str, k: int) -> str:
        """Returns the decoded input string letter at index k

        Proposed solution which only computes k.
        Overall time and complexity is O(N).

        Args:
            s (str): the encoded input, digits are special repeat instructions
                letters are letters
            k (int): the index (1-indexed) of the letter to return in the
                decoded string

        Returns:
            str: the letter at k index in the decoded string
        """
        # Total length of the decoded string
        total_length = 0
        # A place to keep our current index
        idx = 0

        # Calculate the total length  of the decoded string
        while total_length < k:
            c = s[idx]
            if c.isdigit():
                # Multiply total_length by the digit
                total_length *= int(c)
            else:
                # Increment total_length for a letter
                total_length += 1
            # Move to the next character in the input
            idx += 1

        # Backtrack to find the kth letter
        # Move back to the last character
        idx -= 1
        while True:
            c = s[idx]
            if c.isdigit():
                # Divide total_length by the digit
                total_length /= int(c)
                # Update k based on the remainder
                k %= total_length
            else:
                if k % total_length == 0:
                    # If k is a multiple of total_length, return the letter
                    return c
                # Decrement total_length for a letter
                total_length -= 1
            # Move to the previous character in the input string
            idx -= 1
