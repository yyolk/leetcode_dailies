# https://leetcode.com/problems/words-within-two-edits-of-dictionary

class Solution:
    """2452. Words Within Two Edits of Dictionary
    
    You are given two string arrays, queries and dictionary. All words in each array
    comprise of lowercase English letters and have the same length.
    In one edit you can take a word from queries, and change any letter in it to any
    other letter. Find all words from queries that, after a maximum of two edits,
    equal some word from dictionary.
    Return a list of all words from queries, that match with some word from
    dictionary after a maximum of two edits. Return the words in the same order they
    appear in queries.
    """
    def two_edit_words(self, queries: list[str], dictionary: list[str]) -> list[str]:
        # result collects matching queries in original order
        result = []
        for q in queries:
            for d in dictionary:
                # count differing positions (hamming distance)
                diffs = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diffs += 1
                        # early exit: more than two edits already needed
                        if diffs > 2:
                            break
                if diffs <= 2:
                    result.append(q)
                    # one valid dictionary match found; skip remaining words
                    break
        return result

    twoEditWords = two_edit_words