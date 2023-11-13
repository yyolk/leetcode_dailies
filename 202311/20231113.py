# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    """2785. Sort Vowels in a String

    Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:

    * All consonants remain in their original places. More formally, if there is an
    index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] =
    s[i]`.

    * The vowels must be sorted in the **nondecreasing** order of their **ASCII**
    values. More formally, for pairs of indices `i`, `j` with `0 <= i < j < s.length`
    such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII
    value than `t[j]`.

    Return *the resulting string*.

    The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in
    lowercase or uppercase. Consonants comprise all letters that are not vowels.
    """

    def sort_vowels(self, s: str) -> str:
        """
        Sort the string in accordance to the sort by vowel rules.

        Args:
            s: The input string to sort characters.

        Returns:
            The resulting, sorted string.
        """
        vowels = set("aeiouAEIOU")
        consonants = [c for c in s if c not in vowels]

        sorted_vowels = sorted([v for v in s if v in vowels], reverse=True)
        result = ""

        for char in s:
            if char in vowels:
                # Pick one from sorted_vowels
                result += sorted_vowels.pop()
            else:
                result += char

        return result

    sortVowels = sort_vowels
