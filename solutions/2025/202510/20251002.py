# https://leetcode.com/problems/water-bottles-ii/


class Solution:
    """3100. Water Bottles II

    You are given two integers `num_bottles` and `num_exchange`.

    `num_bottles` represents the number of full water bottles that you initially have.
    In one operation, you can perform one of the following operations:

    * Drink any number of full water bottles turning them into empty bottles.

    * Exchange `num_exchange` empty bottles with one full water bottle. Then, increase
    `num_exchange` by one.

    Note that you cannot exchange multiple batches of empty bottles for the same value
    of `num_exchange`. For example, if `num_bottles == 3` and `num_exchange == 1`, you
    cannot exchange `3` empty water bottles for `3` full bottles.

    Return *the **maximum** number of water bottles you can drink*."""

    def max_bottles_drunk(self, num_bottles: int, num_exchange: int) -> int:
        # Initialize with all initial bottles drunk and turned into empties
        drunk = num_bottles
        empty = num_bottles
        # Continue exchanging as long as there are enough empties for the current exchange rate
        while empty >= num_exchange:
            # Spend the required empties for one exchange
            empty -= num_exchange
            # Increase the exchange rate for the next potential exchange
            num_exchange += 1
            # Account for drinking the newly acquired full bottle
            drunk += 1
            # Add the empty from the drunk bottle
            empty += 1
        # Return the total bottles drunk
        return drunk

    maxBottlesDrunk = max_bottles_drunk
