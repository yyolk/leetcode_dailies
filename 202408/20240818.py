# https://leetcode.com/problems/ugly-number-ii/
import heapq


class Solution:
    """264. Ugly Number II

    An **ugly number** is a positive integer whose prime factors are limited to `2`,
    `3`, and `5`.

    Given an integer `n`, return *the* `nth` ***ugly number***.

    """

    def nth_ugly_number(self, n: int) -> int:
        # Initialize a min heap
        heap = [1]
        # To keep track of the visited numbers
        visited = set(heap)
        # The prime factors
        primes = [2, 3, 5]

        # Pop the smallest element from the heap n times
        for _ in range(n):
            # Get the smallest number from the heap
            ugly = heapq.heappop(heap)
            # Generate new ugly numbers by multiplying with each prime factor
            for prime in primes:
                new_ugly = ugly * prime
                # Only add to the heap if it's not already visited
                if new_ugly not in visited:
                    heapq.heappush(heap, new_ugly)
                    visited.add(new_ugly)

        # The nth ugly number is stored in `ugly` after the loop
        return ugly

    nthUglyNumber = nth_ugly_number
