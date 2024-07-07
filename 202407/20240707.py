# https://leetcode.com/problems/water-bottles/


class Solution:
    """1518. Water Bottles

    There are `num_bottles` water bottles that are initially full of water. You can
    exchange `num_exchange` empty water bottles from the market with one full water
    bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Given the two integers `num_bottles` and `num_exchange`, return *the **maximum**
    number of water bottles you can drink*.

    """

    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        # Base case: if the number of bottles is less than the exchange rate,
        # return the number of bottles because no more exchanges can be made
        if num_bottles < num_exchange:
            return num_bottles
        
        # Calculate the new full bottles obtained from exchange
        # Recursive call: Total drunk bottles are the exchange rate (num_exchange) plus
        # the result of the recursive call with the new number of bottles obtained after exchange        
        return num_exchange + self.num_water_bottles(num_bottles - num_exchange + 1, num_exchange)

    numWaterBottles = num_water_bottles
