# https://leetcode.com/problems/word-break-ii/


class Solution:
    """140. Word Break II

    Given a string `s` and a dictionary of strings `word_dict`, add spaces in `s` to
    construct a sentence where each word is a valid dictionary word. Return all such
    possible sentences in **any order**.

    **Note** that the same word in the dictionary may be reused multiple times in the
    segmentation.

    """

    def word_break(self, s: str, word_dict: list[str]) -> list[str]:
        # Create a set for faster lookups
        word_set = set(word_dict)
        # Memoization dictionary to store results for substrings
        memo = {}

        def backtrack(start):
            # If we've already computed this substring, return the result
            if start in memo:
                return memo[start]
            # If we've reached the end of the string, return an empty list (base case)
            if start == len(s):
                return [""]

            # List to store the sentences formed from the current substring
            sentences = []
            # Try every possible end index for the current substring
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                # If the word is in the dictionary, recursively solve for the remaining substring
                if word in word_set:
                    for sub_sentence in backtrack(end):
                        # If sub_sentence is not empty, add a space between the words
                        if sub_sentence:
                            sentences.append(word + " " + sub_sentence)
                        else:
                            sentences.append(word)
            
            # Memoize the result for the current start index
            memo[start] = sentences
            return sentences

        # Start the recursion from the beginning of the string
        return backtrack(0)

    wordBreak = word_break
