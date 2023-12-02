# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from collections import Counter


class Solution:
    """1160. Find Words That Can Be Formed by Characters

    You are given an array of strings `words` and a string `chars`.

    A string is **good** if it can be formed by characters from chars (each character
    can only be used once).

    Return *the sum of lengths of all good strings in words*.
    """

    def count_characters(self, words: list[str], chars: str) -> int:
        """Count all the characters in *good strings*.

        Args:
            words: Input list of strings that are the words.
            chars: Predicate characters.

        Returns:
            Sum of lengths of all good strings in words.
        """
        # Count every character in predicate sequence.
        chars_counter = Counter(chars)

        # Initialize running total
        total = 0

        for word in words:
            # Create a Counter object for the characters in the current word.
            word_counter = Counter(word)

            # Check to see if word_counter is a sub-multiset of chars_counter.
            if word_counter <= chars_counter:
                # If it is, add the current length of word to the running total.
                total += len(word)

        return total

    countCharacters = count_characters
