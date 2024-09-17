# https://leetcode.com/problems/uncommon-words-from-two-sentences/
from collections import Counter


class Solution:
    """884. Uncommon Words from Two Sentences

    A **sentence** is a string of single\\-space separated words where each word consists
    only of lowercase letters.

    A word is **uncommon** if it appears exactly once in one of the sentences, and
    **does not appear** in the other sentence.

    Given two **sentences** `s1` and `s2`, return *a list of all the **uncommon
    words***. You may return the answer in **any order**.

    """

    def uncommon_from_sentences(self, s1: str, s2: str) -> list[str]:
        # Combine both sentences and split into words
        words = (s1 + ' ' + s2).split()
        
        # Count occurrences of each word
        word_count = Counter(words)
        
        # Filter words that appear exactly once
        uncommon_words = [word for word, count in word_count.items() if count == 1]
        
        return uncommon_words

    uncommonFromSentences = uncommon_from_sentences
