# https://leetcode.com/problems/best-sightseeing-pair/


class Solution:
    """1014. Best Sightseeing Pair

    You are given an integer array `values` where values[i] represents the value of the
    `ith` sightseeing spot. Two sightseeing spots `i` and `j` have a **distance** `j -
    i` between them.

    The score of a pair (`i < j`) of sightseeing spots is `values[i] + values[j] + i -
    j`: the sum of the values of the sightseeing spots, minus the distance between them.

    Return *the maximum score of a pair of sightseeing spots*."""

    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        # Initialize the maximum score with the first pair possible
        max_score = 0
        # Keep track of the maximum of (values[i] + i) seen so far
        max_i = values[0] + 0
        
        for j in range(1, len(values)):
            # For each j, calculate the score with the best i seen so far
            current_score = max_i + values[j] - j
            max_score = max(max_score, current_score)
            
            # Update max_i for the next iteration
            max_i = max(max_i, values[j] + j)
        
        return max_score

    maxScoreSightseeingPair = max_score_sightseeing_pair
