# https://leetcode.com/problems/word-break/


class Solution:
    """139. Word Break

    Given a string `s` and a dictionary of strings `word_dict`, return `true` if `s` can
    be segmented into a space-separated sequence of one or more dictionary words.

    **Note** that the same word in the dictionary may be reused multiple times in the
    segmentation.

    """

    def word_break(self, s: str, word_dict: list[str]) -> bool:
        # Create a set for faster word lookup
        word_set = set(word_dict)

        # Create a list to store whether a substring ending at index i can be segmented
        dp = [False] * (len(s) + 1)
        # An empty string can be segmented
        dp[0] = True

        # Iterate through each index in s
        for i in range(1, len(s) + 1):
            # Iterate through each index before i
            for j in range(i):
                # Check if the substring from j to i exists in the word set
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # Once found, no need to check further
                    break

        return dp[len(s)]

    wordBreak = word_break
