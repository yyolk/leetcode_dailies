# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/


class Solution:
    """3403. Find the Lexicographically Largest String From the Box I

    You are given a string `word`, and an integer `num_friends`.

    Alice is organizing a game for her `num_friends` friends. There are multiple rounds
    in the game, where in each round:

    * `word` is split into `num_friends` **non-empty** strings, such that no previous
    round has had the **exact** same split.

    * All the split words are put into a box.

    Find the lexicographically largest string from the box after all the rounds are
    finished."""

    def answer_string(self, word: str, num_friends: int) -> str:
        m = len(word) - num_friends + 1  # splits to be done with m length 
        if num_friends == 1:  # if only one split we can do total word is taken 
            return word
        # else check all m length splits and find max in them 
        return max(word[i:i+m] for i in range(len(word) - m + 1))

    answerString = answer_string
