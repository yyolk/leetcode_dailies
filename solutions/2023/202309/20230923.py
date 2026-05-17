# https://leetcode.com/problems/longest-string-chain/


class Solution:
    """1048. Longest String Chain

    You are given an array of `words` where each word consists of lowercase English letters.

    `wordA` is a **predecessor** of `wordB` if and only if we can insert **exactly one**
    letter anywhere in `wordA` **without changing the order of the other characters** to
    make it equal to `wordB`.

    * For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a
    **predecessor** of `"bcad"`.

    A **word chain**is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where
    `word1` is a **predecessor** of `word2`, `word2` is a **predecessor** of `word3`, and so
    on. A single word is trivially a **word chain** with `k == 1`.

    Return *the **length** of the **longest possible word chain** with words chosen from the
    given list of* `words`.
    """

    def longestStrChain(self, words: list[str]) -> int:
        """Calculate the longest chain of words that appear in the input

        Proposed solution using dynamic programming

        Args:
            words (list of str): the input sequence of letter sequences to compute
                sequential chains from

        Returns:
            int: the length of the longest possible word chain from input
        """
        # Sort words by length in ascending order
        words.sort(key=len)

        # Dict to store length of the longest chain for each word
        word_chain_lengths = {}

        # Initialize max_chain_length to 1 (for trivial chains)
        max_chain_length = 1

        # Iterate through the words
        for word in words:
            # Initialize the chain length for the current word to 1
            word_chain_lengths[word] = 1

            # Generate all possible predecessors by removing one character at a time
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1 :]

                # If the predecessor is in the dictionary, update the chain length
                if predecessor in word_chain_lengths:
                    word_chain_lengths[word] = max(
                        word_chain_lengths[word], word_chain_lengths[predecessor] + 1
                    )

            # Update max_chain_length, for every iteration
            max_chain_length = max(max_chain_length, word_chain_lengths[word])

        # max_chain_length is the final max_chain_length after iterating
        return max_chain_length
