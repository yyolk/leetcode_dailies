# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/


class Solution:
    """2554. Maximum Number of Integers to Choose From a Range I

    You are given an integer array `banned` and two integers `n` and `max_sum`. You are
    choosing some number of integers following the below rules:

    * The chosen integers have to be in the range `[1, n]`.

    * Each integer can be chosen **at most once**.

    * The chosen integers should not be in the array `banned`.

    * The sum of the chosen integers should not exceed `max_sum`.

    Return *the **maximum** number of integers you can choose following the mentioned
    rules*."""

    def max_count(self, banned: list[int], n: int, max_sum: int) -> int:
        # Convert banned to a set for O(1) lookup time
        banned_set = set(banned)
        count = 0
        current_sum = 0
        
        # Iterate through the range from 1 to n
        for num in range(1, n + 1):
            if num not in banned_set:
                # If adding this number doesn't exceed max_sum, add it
                if current_sum + num <= max_sum:
                    current_sum += num
                    count += 1
                else:
                    # If adding this number would exceed max_sum, we stop here
                    break
        
        return count

    maxCount = max_count
