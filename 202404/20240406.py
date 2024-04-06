# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    """1249. Minimum Remove to Make Valid Parentheses

    Given a string s of `'('` , `')'` and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any
    positions ) so that the resulting *parentheses string* is valid and return **any**
    valid string.

    Formally, a *parentheses string* is valid if and only if:

    * It is the empty string, contains only lowercase characters, or

    * It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid
    strings, or

    * It can be written as `(A)`, where `A` is a valid string.

    """

    def min_remove_to_make_valid(self, s: str) -> str: ...

    minRemoveToMakeValid = min_remove_to_make_valid
