# https://leetcode.com/problems/maximum-score-words-formed-by-letters/


class Solution:
    """1255. Maximum Score Words Formed by Letters

    Given a list of `words`, list of  single `letters` (might be repeating) and `score`
    of every character.

    Return the maximum score of **any** valid set of words formed by using the given
    letters (`words[i]` cannot be used two or more times).

    It is not necessary to use all characters in `letters` and each letter can only be
    used once. Score of letters `'a'`, `'b'`, `'c'`, ... ,`'z'` is given by `score[0]`,
    `score[1]`, ... , `score[25]` respectively.

    """

    def max_score_words(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int: ...

    maxScoreWords = max_score_words
