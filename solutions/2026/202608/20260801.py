# https://leetcode.com/problems/predict-the-winner/
from functools import cache


class Solution:
    """486. Predict the Winner

    You are given an integer array `nums`. Two players are playing a game with this
    array: player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. Both players start
    the game with a score of `0`. At each turn, the player takes one of the numbers from
    either end of the array (i.e., `nums[0]` or `nums[nums.length - 1]`) which reduces
    the size of the array by `1`. The player adds the chosen number to their score. The
    game ends when there are no more elements in the array.

    Return `true` if Player 1 can win the game. If the scores of both players are equal,
    then player 1 is still the winner, and you should also return `true`. You may assume
    that both players are playing optimally.

    Constraints:

    * `1 <= nums.length <= 20`

    * `0 <= nums[i] <= 107`"""

    def predict_the_winner(self, nums: list[int]) -> bool:
        @cache
        def best_score_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            take_left = nums[left] - best_score_diff(left + 1, right)
            take_right = nums[right] - best_score_diff(left, right - 1)
            return max(take_left, take_right)

        return best_score_diff(0, len(nums) - 1) >= 0

    predictTheWinner = predict_the_winner
