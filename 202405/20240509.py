# https://leetcode.com/problems/maximize-happiness-of-selected-children/


class Solution:
    """3075. Maximize Happiness of Selected Children

    You are given an array `happiness` of length `n`, and a **positive** integer `k`.

    There are `n` children standing in a queue, where the `ith` child has **happiness
    value** `happiness[i]`. You want to select `k` children from these `n` children in
    `k` turns.

    In each turn, when you select a child, the **happiness value** of all the children
    that have **not** been selected till now decreases by `1`. Note that the happiness
    value **cannot** become negative and gets decremented **only** if it is positive.

    Return *the **maximum** sum of the happiness values of the selected children you can
    achieve by selecting* `k` *children*.

    """

    def maximum_happiness_sum(self, happiness: list[int], k: int) -> int:
        selected = 0
        max_sum = 0

        # Sort the children by their happiness values in descending order
        happiness.sort(reverse=True)

        # Iterate through the first k children
        for score in happiness:
            # Check if the required number of children is selected
            if selected == k:
                return max_sum
            # Add their happiness value to the maximum sum
            max_sum += max(0, score - selected)
            # Increment the count of selected children
            selected += 1

        return max_sum

    maximumHappinessSum = maximum_happiness_sum
