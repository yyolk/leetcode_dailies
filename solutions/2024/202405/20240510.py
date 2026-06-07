# https://leetcode.com/problems/k-th-smallest-prime-fraction/
from heapq import heappop, heappush


class Solution:
    """786. K-th Smallest Prime Fraction

    You are given a sorted integer array `arr` containing `1` and **prime** numbers,
    where all the integers of `arr` are unique. You are also given an integer `k`.

    For every `i` and `j` where `0 <= i < j < arr.length`, we consider the fraction
    `arr[i] / arr[j]`.

    Return *the* `kth` *smallest fraction considered*. Return your answer as an array of
    integers of size `2`, where `answer[0] == arr[i]` and `answer[1] == arr[j]`.

    """

    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        # Create a min heap to store fractions and their corresponding pairs
        min_heap = []
        n = len(arr)
        # Generate all possible fractions and add them to the min heap
        for i in range(n):
            for j in range(i + 1, n):
                heappush(min_heap, (arr[i] / arr[j], (arr[i], arr[j])))
        # Pop k elements from the min heap to get the kth smallest fraction
        for _ in range(k):
            a, b = heappop(min_heap)[1]
        # Return the kth smallest fraction
        return [a, b]

    kthSmallestPrimeFraction = kth_smallest_prime_fraction
