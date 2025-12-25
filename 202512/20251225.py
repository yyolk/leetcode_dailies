# https://leetcode.com/problems/maximize-happiness-of-selected-children


class Solution:
    """3075. Maximize Happiness of Selected Children

    You are given an array happiness of length n, and a positive integer k.
    There are n children standing in a queue, where the ith child has
    happiness value happiness[i]. You want to select k children in k turns.
    In each turn, when you select a child, the happiness value of all the
    children that have not been selected till now decreases by 1. Note that
    the happiness value cannot become negative and gets decremented only if
    it is positive.
    Return the maximum sum of the happiness values of the selected children
    you can achieve by selecting k children.
    """
    def maximum_happiness_sum(self, happiness: list[int], k: int) -> int:
        # Sort in descending order to always consider the current highest
        happiness.sort(reverse=True)
        
        total = 0
        for i in range(k):
            # After i turns, all remaining children have lost i happiness
            # Effective happiness of the i-th best child is max(0, original - i)
            curr = happiness[i] - i
            if curr <= 0:
                break  # No further selections can add positive happiness
            total += curr
        return total

    maximumHappinessSum = maximum_happiness_sum