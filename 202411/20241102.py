# https://leetcode.com/problems/circular-sentence/


class Solution:
    """2490. Circular Sentence

    A **sentence** is a list of words that are separated by a **single** space with no
    leading or trailing spaces.

    * For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all
    sentences.

    Words consist of **only** uppercase and lowercase English letters. Uppercase and
    lowercase English letters are considered different.

    A sentence is **circular** if:

    * The last character of a word is equal to the first character of the next word.

    * The last character of the last word is equal to the first character of the first
    word.

    For example, `"leetcode exercises sound delightful"`, `"eetcode"`, `"leetcode eats
    soul"` are all circular sentences. However, `"Leetcode is cool"`, `"happy
    Leetcode"`, `"Leetcode"` and `"I like Leetcode"` are **not** circular sentences.

    Given a string `sentence`, return `true` *if it is circular*. Otherwise, return
    `false`.

    """

    def is_circular_sentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check if the sentence has at least one word
        if not words:
            return False
        
        # Check circularity for all adjacent words
        for i in range(len(words)):
            # Check the last word with the first word for circularity
            if i == len(words) - 1:
                if words[i][-1] != words[0][0]:
                    return False
            # Check adjacent words for circularity
            elif words[i][-1] != words[i+1][0]:
                return False

        return True

    isCircularSentence = is_circular_sentence
