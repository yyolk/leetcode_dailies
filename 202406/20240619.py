# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/


class Solution:
    """1482. Minimum Number of Days to Make m Bouquets

    You are given an integer array `bloom_day`, an integer `m` and an integer `k`.

    You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent
    flowers** from the garden.

    The garden consists of `n` flowers, the `ith` flower will bloom in the
    `bloom_day[i]` and then can be used in **exactly one** bouquet.

    Return *the minimum number of days you need to wait to be able to make* `m`
    *bouquets from the garden*. If it is impossible to make m bouquets return `-1`.

    """

    def min_days(self, bloom_day: list[int], m: int, k: int) -> int:
        # Helper function to check if we can make m bouquets in 'days'
        def can_make_bouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloom_day:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        # If it's not possible to make m bouquets
        if m * k > len(bloom_day):
            return -1

        left, right = min(bloom_day), max(bloom_day)
        while left < right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left

    minDays = min_days
