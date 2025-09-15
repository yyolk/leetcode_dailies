# https://leetcode.com/problems/maximum-number-of-words-you-can-type/


class Solution:
    """1935. Maximum Number of Words You Can Type

    There is a malfunctioning keyboard where some letter keys do not work. All other
    keys on the keyboard work properly.

    Given a string `text` of words separated by a single space (no leading or trailing
    spaces) and a string `broken_letters` of all **distinct** letter keys that are
    broken, return *the **number of words** in* `text` *you can fully type using this
    keyboard*."""

    def can_be_typed_words(self, text: str, broken_letters: str) -> int: ...

    canBeTypedWords = can_be_typed_words
