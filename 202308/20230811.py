# https://leetcode.com/problems/coin-change-ii/


class Solution:
    """518. Coin Change II

    You are given an integer array `coins` representing coins of different denominations
    and an integer `amount` representing a total amount of money.

    Return *the number of combinations that make up that amount*. If that amount of
    money cannot be made up by any combination of the coins, return `0`.

    You may assume that you have an infinite number of each kind of coin.

    The answer is **guaranteed** to fit into a signed **32-bit** integer.

    """

    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to store the number of combinations for each amount from 0 to the target amount
        dp = [0] * (amount + 1)
        
        # There is one way to make change for amount 0, i.e., not using any coin
        dp[0] = 1
        
        # Iterate through each coin and update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        # The final result is stored in the last element of the dp array
        return dp[amount]

    change = change
