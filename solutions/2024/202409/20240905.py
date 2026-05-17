# https://leetcode.com/problems/find-missing-observations/


class Solution:
    """2028. Find Missing Observations

    You have observations of `n + m` **6\\-sided** dice rolls with each face numbered
    from `1` to `6`. `n` of the observations went missing, and you only have the
    observations of `m` rolls. Fortunately, you have also calculated the **average
    value** of the `n + m` rolls.

    You are given an integer array `rolls` of length `m` where `rolls[i]` is the value
    of the `ith` observation. You are also given the two integers `mean` and `n`.

    Return *an array of length* `n` *containing the missing observations such that the
    **average value** of the* `n + m` *rolls is **exactly*** `mean`. If there are
    multiple valid answers, return *any of them*. If no such array exists, return *an
    empty array*.

    The **average value** of a set of `k` numbers is the sum of the numbers divided by
    `k`.

    Note that `mean` is an integer, so the sum of the `n + m` rolls should be divisible
    by `n + m`.

    """

    def missing_rolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        # Total number of rolls
        total_rolls = len(rolls) + n

        # Total sum if the mean were exact
        total_sum = mean * total_rolls

        # Sum of the observed rolls
        observed_sum = sum(rolls)

        # Sum of the missing rolls
        missing_sum = total_sum - observed_sum

        # Check if it's possible to achieve this sum with n rolls of a 6-sided die
        if missing_sum < n or missing_sum > 6 * n:
            return []

        # Initialize missing rolls with the minimum possible value (1)
        missing_rolls = [1] * n

        # Distribute the remaining sum
        remaining_sum = (
            missing_sum - n
        )  # Subtract n because we've already added 1 to each roll

        for i in range(n):
            # Add as much as possible to the current roll without exceeding 6
            add = min(remaining_sum, 5)  # 5 because we started from 1, so 1 + 5 = 6 max
            missing_rolls[i] += add
            remaining_sum -= add
            if remaining_sum == 0:
                break

        return missing_rolls

    missingRolls = missing_rolls
