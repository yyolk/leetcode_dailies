# https://leetcode.com/problems/four-divisors


class Solution:
    """1390. Four Divisors

    Given an integer array nums, return the sum of divisors of the integers
    in that array that have exactly four divisors. If there is no such
    integer in the array, return 0.
    """
    def sum_four_divisors(self, nums: list[int]) -> int:
        total = 0
        for n in nums:
            # Find divisors efficiently by checking up to sqrt(n)
            count = 0          # number of divisors found
            divisor_sum = 0    # sum of divisors
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    # i is a divisor
                    count += 1
                    divisor_sum += i
                    # corresponding pair divisor (unless perfect square)
                    if i != n // i:
                        count += 1
                        divisor_sum += n // i
            # Numbers with exactly 4 divisors are either p^3 or p*q (distinct primes)
            if count == 4:
                total += divisor_sum
        return total

    sumFourDivisors = sum_four_divisors