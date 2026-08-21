# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/


import math


class Solution:
    """3116. Kth Smallest Amount With Single Denomination Combination

    You are given an integer array `coins` representing coins of different denominations
    and an integer `k`.

    You have an infinite number of coins of each denomination. However, you are **not
    allowed** to combine coins of different denominations.

    Return the `kth` **smallest** amount that can be made using these coins.

    Constraints:

    * `1 <= coins.length <= 15`

    * `1 <= coins[i] <= 25`

    * `1 <= k <= 2 * 109`

    * `coins` contains pairwise distinct integers."""

    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        """Return the kth smallest positive amount divisible by at least one coin."""
        coins = sorted(coins)
        filtered: list[int] = []
        for coin in coins:
            if all(coin % base != 0 for base in filtered):
                filtered.append(coin)

        if filtered[0] == 1:
            return k

        n = len(filtered)
        lcms = [1] * (1 << n)
        signs = [0] * (1 << n)

        for mask in range(1, 1 << n):
            low_bit = mask & -mask
            bit_idx = low_bit.bit_length() - 1
            prev = mask ^ low_bit
            lcms[mask] = lcms[prev] * filtered[bit_idx] // math.gcd(
                lcms[prev], filtered[bit_idx]
            )
            signs[mask] = 1 if mask.bit_count() % 2 == 1 else -1

        def count(amount: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                lcm_value = lcms[mask]
                if lcm_value <= amount:
                    total += signs[mask] * (amount // lcm_value)
            return total

        left, right = 1, filtered[0] * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left

    findKthSmallest = find_kth_smallest
