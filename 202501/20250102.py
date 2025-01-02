# https://leetcode.com/problems/count-vowel-strings-in-ranges/


class Solution:
    """2559. Count Vowel Strings in Ranges

    You are given a **0-indexed** array of strings `words` and a 2D array of integers
    `queries`.

    Each query `queries[i] = [li, ri]` asks us to find the number of strings present in
    the range `li` to `ri` (both **inclusive**) of `words` that start and end with a
    vowel.

    Return *an array* `ans` *of size* `queries.length`*, where* `ans[i]` *is the answer
    to the* `i`th *query*.

    **Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`."""

    def vowel_strings(
        self, words: list[str], queries: list[list[int]]
    ) -> list[int]:
        vowels = set("aeiou")
        
        # Helper function to check if a word starts and ends with a vowel
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels
        
        # Count vowel strings for each index in words
        count = [0] * (len(words) + 1)
        for i, word in enumerate(words, 1):
            count[i] = count[i-1] + (1 if is_vowel_string(word) else 0)
        
        # Process queries
        ans = []
        for li, ri in queries:
            # The count at ri + 1 minus count at li gives us the number of vowel strings in the range
            ans.append(count[ri + 1] - count[li])
        
        return ans

    vowelStrings = vowel_strings
