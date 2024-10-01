# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/


class Solution:
    """1497. Check If Array Pairs Are Divisible by k

    Given an array of integers `arr` of even length `n` and an integer `k`.

    We want to divide the array into exactly `n / 2` pairs such that the sum of each
    pair is divisible by `k`.

    Return `true` *If you can find a way to do that or* `false` *otherwise*.

    """

    def can_arrange(self, arr: list[int], k: int) -> bool:
        # Count the frequency of each remainder when divided by k
        remainder_count = Counter(num % k for num in arr)
        
        # Check if the count of numbers with remainder 0 is even
        if remainder_count[0] % 2 != 0:
            return False
        
        # Check for other remainders from 1 to k//2 (inclusive)
        for i in range(1, k // 2 + 1):
            if remainder_count[i] != remainder_count.get(k - i, 0):
                return False
        
        # If all checks passed, we can arrange the array
        return True

    canArrange = can_arrange
