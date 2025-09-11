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

    The vowels are `"a"`, `"e"`, `"i"`, `"o"`, and `"u"`, and they can appear in
    lowercase or uppercase. Consonants comprise all letters that are not vowels."""

    def sort_vowels(self, s: str) -> str:
        # Define the set of vowels (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")
        
        # Extract all vowels from the string s into a list
        vowel_list = [c for c in s if c in vowels]
        
        # Sort the vowel list in non-decreasing ASCII order
        vowel_list.sort()
        
        # Initialize result list and index for sorted vowels
        result = []
        j = 0
        
        # Iterate through each character in s
        for c in s:
            if c in vowels:
                # Replace vowel with the next sorted vowel
                result.append(vowel_list[j])
                j += 1
            else:
                # Keep consonant in place
                result.append(c)
        
        # Join the result list into a string
        return "".join(result)

    sortVowels = sort_vowels
