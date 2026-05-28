# https://leetcode.com/problems/longest-common-suffix-queries/

class Solution:
    """3093. Longest Common Suffix Queries

    You are given two arrays of strings `words_container` and `words_query`.
    For each `words_query[i]`, you need to find a string from `words_container`
    that has the longest common suffix with `words_query[i]`. If there are two or
    more strings in `words_container` that share the longest common suffix, find
    the string that is the smallest in length. If there are two or more such
    strings that have the same smallest length, find the one that occurred
    earlier in `words_container`.
    Return an array of integers `ans`, where `ans[i]` is the index of the string
    in `words_container` that has the longest common suffix with `words_query[i]`.
    """
    def string_indices(
        self, words_container: list[str], words_query: list[str]
    ) -> list[int]:
        lengths = [len(w) for w in words_container]

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.best = -1

        root = TrieNode()

        # insert each reversed container word; update best (min length then
        # min index) at every node along its path
        for i, word in enumerate(words_container):
            node = root
            # root represents suffix length 0 (all words qualify)
            if (node.best == -1 or
                lengths[i] < lengths[node.best] or
                (lengths[i] == lengths[node.best] and i < node.best)):
                node.best = i
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # deeper node = longer common suffix
                if (node.best == -1 or
                    lengths[i] < lengths[node.best] or
                    (lengths[i] == lengths[node.best] and i < node.best)):
                    node.best = i

        # answer each query
        ans = []
        for q in words_query:
            node = root
            best = node.best
            # follow reversed query as far as trie allows
            for char in reversed(q):
                if char not in node.children:
                    break
                node = node.children[char]
                best = node.best
            ans.append(best)
        return ans

    stringIndices = string_indices