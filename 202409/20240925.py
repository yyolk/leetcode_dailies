# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/


class TrieNode:
    def __init__(self):
        self.children = {}
        # Count of words ending here or passing through this node
        self.count = 0


class Solution:
    """2416. Sum of Prefix Scores of Strings

    You are given an array `words` of size `n` consisting of **non\\-empty** strings.

    We define the **score** of a string `word` as the **number** of strings `words[i]`
    such that `word` is a **prefix** of `words[i]`.

    * For example, if `words = ["a", "ab", "abc", "cab"]`, then the score of `"ab"` is
    `2`, since `"ab"` is a prefix of both `"ab"` and `"abc"`.

    Return *an array* `answer` *of size* `n` *where* `answer[i]` *is the **sum** of
    scores of every **non\\-empty** prefix of* `words[i]`.

    **Note** that a string is considered as a prefix of itself.

    """

    def __init__(self):
        self.root = TrieNode()

    def sum_prefix_scores(self, words: list[str]) -> list[int]:
        # Insert all words into Trie
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # Increment count for each character
                node.count += 1

        # Calculate prefix scores for each word
        result = []
        for word in words:
            score = 0
            node = self.root
            for char in word:
                if char not in node.children:
                    # If char not in Trie, no need to continue for this word
                    break
                node = node.children[char]
                # Add the count of this prefix
                score += node.count
            result.append(score)

        return result

    sumPrefixScores = sum_prefix_scores
