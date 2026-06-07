# https://leetcode.com/problems/string-matching-in-an-array/


class Solution:
    """1408. String Matching in an Array

    Given an array of string `words`, return *all strings in* `words` *that is a
    **substring** of another word*. You can return the answer in **any order**.

    A **substring** is a contiguous sequence of characters within a string"""

    def string_matching(self, words: list[str]) -> list[str]:
        # Sort words by length to optimize checking for substrings
        words.sort(key=len)
        result = []

        # Check each word to see if it's a substring of any other word
        for i, word in enumerate(words):
            if any(word in other for other in words[i + 1 :]):
                result.append(word)

        return result

    stringMatching = string_matching
