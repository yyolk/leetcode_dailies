# https://leetcode.com/problems/solving-questions-with-brainpower/


class Solution:
    """2140. Solving Questions With Brainpower

    You are given a **0-indexed** 2D integer array `questions` where `questions[i] =
    [pointsi, brainpoweri]`.

    The array describes the questions of an exam, where you have to process the
    questions **in order** (i.e., starting from question `0`) and make a decision
    whether to **solve** or **skip** each question. Solving question `i` will **earn**
    you `pointsi` points but you will be **unable** to solve each of the next
    `brainpoweri` questions. If you skip question `i`, you get to make the decision on
    the next question.

    * For example, given `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`:

      + If question `0` is solved, you will earn `3` points but you will be unable to
    solve questions `1` and `2`.

      + If instead, question `0` is skipped and question `1` is solved, you will earn
    `4` points but you will be unable to solve questions `2` and `3`.

    Return *the **maximum** points you can earn for the exam*."""

    def most_points(self, questions: list[list[int]]) -> int:
        N = len(questions)
        # Initialize DP array with size N+1, all zeros
        dp = [0] * (N + 1)

        # Iterate from the last question to the first
        for i in range(N - 1, -1, -1):
            points_i, brainpower_i = questions[i]
            # Next index after skipping brainpower_i questions
            next_idx = min(i + brainpower_i + 1, N)
            # Maximum of solving current question or skipping it
            dp[i] = max(points_i + dp[next_idx], dp[i + 1])

        return dp[0]

    mostPoints = most_points
