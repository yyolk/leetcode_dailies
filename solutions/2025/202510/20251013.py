# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/


class Solution:
    """2273. Find Resultant Array After Removing Anagrams

    You are given a **0-indexed** string array `words`, where `words[i]` consists of
    lowercase English letters.

    In one operation, select any index `i` such that `0 < i < words.length` and `words[i
    - 1]` and `words[i]` are **anagrams**, and **delete** `words[i]` from `words`. Keep
    performing this operation as long as you can select an index that satisfies the
    conditions.

    Return `words` *after performing all operations*. It can be shown that selecting the
    indices for each operation in **any** arbitrary order will lead to the same result.

    An **Anagram** is a word or phrase formed by rearranging the letters of a different
    word or phrase using all the original letters exactly once. For example, `"dacb"` is
    an anagram of `"abdc"`."""

    def remove_anagrams(self, words: list[str]) -> list[str]:
        # Initialize an empty list to build the result
        result = []
        # Process each word in the input list
        for word in words:
            # Check if result is empty or current word is not an anagram of the last in result
            # Anagram check via sorting characters for frequency comparison
            if not result or sorted(result[-1]) != sorted(word):
                # Append the word if condition met
                result.append(word)
            # Else skip (effectively delete) the word as it's an anagram of the previous
        # Return the final list after all operations simulated
        return result

    removeAnagrams = remove_anagrams
