# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/


class Solution:
    """3302. Find the Lexicographically Smallest Valid Sequence

    You are given two strings `word1` and `word2`.

    A string `x` is called **almost equal** to `y` if you can change **at most** one
    character in `x` to make it *identical* to `y`.

    A sequence of indices `seq` is called **valid** if:

    * The indices are sorted in **ascending** order.

    * *Concatenating* the characters at these indices in `word1` in **the same** order
    results in a string that is **almost equal** to `word2`.

    Return an array of size `word2.length` representing the lexicographically smallest
    **valid** sequence of indices. If no such sequence of indices exists, return an
    **empty** array.

    **Note** that the answer must represent the *lexicographically smallest array*,
    **not** the corresponding string formed by those indices.

    Constraints:

    * `1 <= word2.length < word1.length <= 3 * 105`

    * `word1` and `word2` consist only of lowercase English letters."""

    def valid_sequence(self, word1: str, word2: str) -> list[int]:
        """...

        Proposed solution ...

        Args:
            word1 (str): ...
            word2 (str): ...

        Returns:
            list of int: ..."""
        ...

    validSequence = valid_sequence
