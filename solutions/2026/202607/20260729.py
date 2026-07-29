# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/


class Solution:
    """3518. Smallest Palindromic Rearrangement II

    You are given a **palindromic** string `s` and an integer `k`.

    Return the **k-th** **lexicographically smallest** palindromic permutation of `s`.
    If there are fewer than `k` distinct palindromic permutations, return an empty
    string.

    **Note:** Different rearrangements that yield the same palindromic string are
    considered identical and are counted once.

    Constraints:

    * `1 <= s.length <= 104`

    * `s` consists of lowercase English letters.

    * `s` is guaranteed to be palindromic.

    * `1 <= k <= 106`"""

    def smallest_palindrome(self, s: str, k: int) -> str: ...

    smallestPalindrome = smallest_palindrome
