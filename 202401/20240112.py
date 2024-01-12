# https://leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution:
    """1704. Determine if String Halves Are Alike

    You are given a string `s` of even length. Split this string into two halves of
    equal lengths, and let `a` be the first half and `b` be the second half.

    Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`,
    `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s` contains
    uppercase and lowercase letters.

    Return `true` *if* `a` *and* `b` *are **alike***. Otherwise, return `false`.
    """

    def halves_are_alike(self, s: str) -> bool:
        def count_vowels(string: str) -> int:
            """Helper function to count vowels in a given string."""
            vowels = set("aeiouAEIOU")
            return sum(1 for char in string if char in vowels)

        # Split the input into two halves.
        length = len(s) // 2
        a, b = s[:length], s[length:]

        # Count vowels on both sides and compare.
        return count_vowels(a) == count_vowels(b)

    halvesAreAlike = halves_are_alike
