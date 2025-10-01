# https://leetcode.com/problems/water-bottles/


class Solution:
    """1518. Water Bottles

    There are `num_bottles` water bottles that are initially full of water. You can
    exchange `num_exchange` empty water bottles from the market with one full water
    bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Given the two integers `num_bottles` and `num_exchange`, return *the **maximum**
    number of water bottles you can drink*."""

    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        # Initialize the total number of bottles drunk
        total_drunk = 0
        # Track the number of empty bottles
        empty_bottles = 0
        # Use a loop to simulate drinking and exchanging until no more full bottles can be obtained
        while num_bottles > 0:
            # Add the current full bottles to the total drunk
            total_drunk += num_bottles
            # Convert the drunk bottles to empty ones
            empty_bottles += num_bottles
            # Calculate how many new full bottles can be obtained by exchanging empties
            num_bottles = empty_bottles // num_exchange
            # Update empties to the remainder after exchange
            empty_bottles = empty_bottles % num_exchange
        # Return the total bottles drunk
        return total_drunk

    numWaterBottles = num_water_bottles
