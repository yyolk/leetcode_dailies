# https://leetcode.com/problems/relative-ranks/


class Solution:
    """506. Relative Ranks

    You are given an integer array `score` of size `n`, where `score[i]` is the score of
    the `ith` athlete in a competition. All the scores are guaranteed to be **unique**.

    The athletes are **placed** based on their scores, where the `1st` place athlete has
    the highest score, the `2nd` place athlete has the `2nd` highest score, and so on.
    The placement of each athlete determines their rank:

    * The `1st` place athlete's rank is `"Gold Medal"`.

    * The `2nd` place athlete's rank is `"Silver Medal"`.

    * The `3rd` place athlete's rank is `"Bronze Medal"`.

    * For the `4th` place to the `nth` place athlete, their rank is their placement
    number (i.e., the `xth` place athlete's rank is `"x"`).

    Return an array `answer` of size `n` where `answer[i]` is the **rank** of the `ith`
    athlete.

    """

    def find_relative_ranks(self, score: list[int]) -> list[str]:
        # Sort scores in descending order to determine ranks
        sorted_scores = sorted(score, reverse=True)

        # Define ranks including special cases for top 3 ranks
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [
            str(i + 1) for i in range(3, len(score))
        ]

        # Map each score to its corresponding rank
        rank_map = {score: rank for score, rank in zip(sorted_scores, ranks)}

        # Generate array of ranks for each athlete based on their scores
        return [rank_map[score] for score in score]

    findRelativeRanks = find_relative_ranks
