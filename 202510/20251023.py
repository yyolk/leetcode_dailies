# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/


class Solution:
    """3461. Check If Digits Are Equal in String After Operations I

    You are given a string `s` consisting of digits. Perform the following operation
    repeatedly until the string has **exactly** two digits:

    * For each pair of consecutive digits in `s`, starting from the first digit,
    calculate a new digit as the sum of the two digits **modulo** 10.

    * Replace `s` with the sequence of newly calculated digits, *maintaining the order*
    in which they are computed.

    Return `true` if the final two digits in `s` are the **same**; otherwise, return
    `false`."""

    def has_same_digits(self, s: str) -> bool: ...

    hasSameDigits = has_same_digits
