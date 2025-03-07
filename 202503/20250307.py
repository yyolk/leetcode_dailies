# https://leetcode.com/problems/closest-prime-numbers-in-range/


class Solution:
    """2523. Closest Prime Numbers in Range

    Given two positive integers `left` and `right`, find the two integers `num1` and
    `num2` such that:

    * `left <= num1 < num2 <= right` .

    * Both `num1` and `num2` are prime numbers.

    * `num2 - num1` is the **minimum** amongst all other pairs satisfying the above
    conditions.

    Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs
    satisfying these conditions, return the one with the **smallest** `num1` value. If
    no such numbers exist, return `[-1, -1]`*.*"""

    def closest_primes(self, left: int, right: int) -> list[int]:
        # If right < 2, there are no prime numbers possible
        if right < 2:
            return [-1, -1]
        
        # Initialize sieve array to mark prime numbers up to right
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        # Sieve of Eratosthenes to mark non-prime numbers
        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        # Collect all primes in the range [left, right]
        # Start from max(left, 2) since primes must be >= 2
        primes = [i for i in range(max(left, 2), right + 1) if is_prime[i]]
        
        # If fewer than 2 primes exist, no pair is possible
        if len(primes) < 2:
            return [-1, -1]
        
        # Find the pair of consecutive primes with minimum difference
        min_diff = float("inf")
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
        
        return ans

    closestPrimes = closest_primes
