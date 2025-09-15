# https://leetcode.com/problems/maximum-number-of-words-you-can-type/


class Solution:
    """1935. Maximum Number of Words You Can Type

    There is a malfunctioning keyboard where some letter keys do not work. All other
    keys on the keyboard work properly.

    Given a string `text` of words separated by a single space (no leading or trailing
    spaces) and a string `broken_letters` of all **distinct** letter keys that are
    broken, return *the **number of words** in* `text` *you can fully type using this
    keyboard*."""

    def can_be_typed_words(self, text: str, broken_letters: str) -> int:
        # Create a set for O(1) lookup of broken letters
        broken_set = set(broken_letters)
        # Split text into words
        words = text.split()
        # Initialize counter for typable words
        count = 0
        # Iterate over each word
        for word in words:
            # Assume word is typable
            can_type = True
            # Check each character in the word
            for char in word:
                # If any char is broken, cannot type this word
                if char in broken_set:
                    can_type = False
                    break
            # If all chars are typable, increment count
            if can_type:
                count += 1
        # Return the number of typable words
        return count

    canBeTypedWords = can_be_typed_words
