# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


class Solution:
    """1662. Check If Two String Arrays are Equivalent

    Given two string arrays `word1` and `word2`, return `True` *if the two arrays
    **represent** the same string, and* `False` *otherwise.*

    A string is **represented** by an array if the array elements concatenated **in
    order** forms the string.
    """

    def array_strings_are_equal(self, word1: list[str], word2: list[str]) -> bool:
        """Determine if the provided input arrays of strings are equal.

        Args:
            word1: The first input list of strings.
            word2: The second input list of strings.

        Returns:
            True if the two arrays represent the same thing, and False otherwise.
        """
        return "".join(word1) == "".join(word2)

    arrayStringsAreEqual = array_strings_are_equal
