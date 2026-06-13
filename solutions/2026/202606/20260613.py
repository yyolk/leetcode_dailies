# https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    """3838. Weighted Word Mapping
    
    You are given an array of strings words, where each string represents a word
    containing lowercase English letters. You are also given an integer array
    weights of length 26, where weights[i] represents the weight of the ith
    lowercase English letter. The weight of a word is defined as the sum of the
    weights of its characters. For each word, take its weight modulo 26 and map
    the result to a lowercase English letter using reverse alphabetical order
    (0 -> 'z', 1 -> 'y', ..., 25 -> 'a'). Return a string formed by
    concatenating the mapped characters for all words in order.
    Constraints:
    * 1 <= words.length <= 100
    * 1 <= words[i].length <= 10
    * weights.length == 26
    * 1 <= weights[i] <= 100
    * words[i] consists of lowercase English letters."""
    def map_word_weights(self, words: list[str], weights: list[int]) -> str:
        res = []
        for word in words:
            # sum weights[char - 'a'] for every char (generator avoids extra list)
            total = sum(weights[ord(c) - ord("a")] for c in word)
            # weight % 26
            mod = total % 26
            # reverse map: 0 -> 'z', ..., 25 -> 'a'
            mapped = chr(ord("z") - mod)
            res.append(mapped)
        # O(N) join is optimal for final concatenation
        return "".join(res)

    mapWordWeights = map_word_weights