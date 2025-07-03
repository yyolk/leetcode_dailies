# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/


class Solution:
    """3304. Find the K-th Character in String Game I

    Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

    You are given a **positive** integer `k`.

    Now Bob will ask Alice to perform the following operation **forever**:

    * Generate a new string by **changing** each character in `word` to its **next**
    character in the English alphabet, and **append** it to the *original* `word`.

    For example, performing the operation on `"c"` generates `"cd"` and performing the
    operation on `"zb"` generates `"zbac"`.

    Return the value of the `kth` character in `word`, after enough operations have been
    done for `word` to have **at least** `k` characters.

    **Note** that the character `'z'` can be changed to `'a'` in the operation."""

    def kth_character(self, k: int) -> str:
        # Calculate the number of 1's in the binary representation of (k-1)
        m = bin(k - 1).count("1")
        # Compute the character by shifting "a" by (m % 26) positions in the alphabet
        return chr((m % 26) + ord("a"))

    kthCharacter = kth_character
