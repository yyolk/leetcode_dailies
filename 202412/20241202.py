# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/


class Solution:
    """1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

    Given a `sentence` that consists of some words separated by a **single space**, and
    a `search_word`, check if `search_word` is a prefix of any word in `sentence`.

    Return *the index of the word in* `sentence` *(**1-indexed**) where* `search_word`
    *is a prefix of this word*. If `search_word` is a prefix of more than one word,
    return the index of the first word **(minimum index)**. If there is no such word
    return `-1`.

    A **prefix** of a string `s` is any leading contiguous substring of `s`."""

    def is_prefix_of_word(self, sentence: str, search_word: str) -> int: ...

    isPrefixOfWord = is_prefix_of_word
