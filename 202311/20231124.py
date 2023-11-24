# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/


class Solution:
    """1561. Maximum Number of Coins You Can Get

    There are `3n` piles of coins of varying size, you and your friends will take piles
    of coins as follows:

    * In each step, you will choose **any** `3` piles of coins (not necessarily
    consecutive).

    * Of your choice, Alice will pick the pile with the maximum number of coins.

    * You will pick the next pile with the maximum number of coins.

    * Your friend Bob will pick the last pile.

    * Repeat until there are no more piles of coins.

    Given an array of integers `piles` where `piles[i]` is the number of coins in the
    `ith` pile.

    Return the maximum number of coins that you can have.
    """

    def max_coins(self, piles: list[int]) -> int:
        """Finds maximum coins you can have.

        Args:
            piles: The piles of coins. Each element is a pile with a number of coins.

        Returns:
            The maximum number of coins you can have.
        """
        # Sort the piles
        piles.sort()

        result = 0

        # Iterate over every third pile starting from the second largest pile.
        for i in range(len(piles) // 3):
            result += piles[-2 - 2 * i]

        return result

    maxCoins = max_coins
